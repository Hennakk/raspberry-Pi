## StepMotor
스텝모터의 내부 구조 모습을 살펴보면 가운데 회전자 영구자석 주변에 코일이 감겨져 있는 고정자(철판)이 있다. 전원 공급 시 고정자에 전자기장이 형성되고 이 전자기력은 영구자석이 자기장에 따라 정렬되도록 유도한다.  

![image](https://user-images.githubusercontent.com/98154707/153051608-ffb2b31d-0b57-4f80-9da9-009be3ba4478.png)  
즉 펄스가 입력될 때 마다 일정한 각도만큼 모터가 회전하도록 제어된다. 이때의 회전각은 스텝각이라고 부른다. 이 스텝각을 작게 하면 모터의 위치를 결정하는 정밀도를 향상시킬 수 있다.   
위의 경우는 하프 스텝 구동으로 첫번째 코일이 여자 된 후 다음 스텝에서 4번과 3번 코일이 동시에 펄스가 입력되면서 회전자가 두개의 코일 사이에 위치하게 된다. 이러한 방식에서 더 나아가 두 개 코일의 전류를 조절하면 이보다 더 세밀하게 스텝을 조절할 수 있다. 회전 각도는 입력 펄스 신호의 수에 비례하고, 회전 속도는 입력 펄스 신호의 주파수에 비례한다.  

![image](https://user-images.githubusercontent.com/98154707/153051918-bef29ccd-7e35-437b-b6e8-49b16c7076b1.png)   ![image](https://user-images.githubusercontent.com/98154707/153051837-8ad2a56e-4d2c-44ae-a338-a12fcc5961db.png)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;싱글 스텝 (4 ->3->2->1)                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   하프 스텝(4->4,3->3->3,2->2->2,1->1)  

참고  https://rasino.tistory.com/149
