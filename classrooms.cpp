#include <iomanip>
#include <iostream>
#include <set>
#include <algorithm> 

using namespace std;

struct Activity{
    int start, end;

    bool operator < (const Activity &other) const {
        if(this->end == other.end){ 
            return this->start < other.start;
        }
        return this->end < other.end;
    }
};

void bubble(int i, int classrooms[], int len){
    while(i < len - 1 && classrooms[i + 1] < classrooms[i]){
        int temp = classrooms[i + 1];
        classrooms[i + 1] = classrooms[i];
        classrooms[i] = temp;
    }
     while(i > 0 && classrooms[i - 1] > classrooms[i]){
        int temp = classrooms[i - 1];
        classrooms[i - 1] = classrooms[i];
        classrooms[i] = temp;
    }

}
int main(){
    int num_activities, num_classrooms;
    cin >> num_activities >> num_classrooms;

    int classrooms[num_classrooms];

    Activity activities[num_activities];
    for(int i = 0; i < num_activities; i++){
        struct Activity a;
        cin >> a.start >> a.end;
    }

    sort(activities, activities + num_activities);

    int num_possible_act = 0;

    for(int i = 0; i < num_activities; i++){
        int k = lower_bound(classrooms, classrooms + num_classrooms, activities[i].start) - classrooms;
        if (classrooms[k] < activities[k].start){
            classrooms[k] = activities[k].end;
            bubble(i, classrooms, num_classrooms);
            num_possible_act += 1;
        }
    }

    cout << num_possible_act << endl;
    
    return 0;
}