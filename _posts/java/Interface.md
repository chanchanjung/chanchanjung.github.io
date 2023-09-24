# Interface

## Inteface란?

인터페이스 개념을 찾아보면 **인터페이스(Interface)는 객체 지향 프로그래밍(OOP)에서 중요한 개념 중 하나로, 추상화와 다형성을 지원하며, 클래스와 클래스 사이의 계약(COntract)을 정의하는데 사용된다** 라고 한다.

하지만 이 개념만 보면 무슨 말인지 잘 모르겠다...

예시를 들어보면

특정 회사에서 사람을 뽑으려고 하는데 자유양식으로 지원서를 받게되면,
대기업 같이 큰 회사에는 지원자가 매우 많아 지원서 확인에 많은 시간이 걸린다.

회사에서는 빠르게 지원서를 확인하고 면접 볼 사람을 뽑아야 하기 때문에 효율적으로 확인하는 방식이 필요하다.

이때 지원서 양식을 제공하는 경우, 지원자들은 동일한 양식의 지원서를 작성하기 때문에 회사에서는 좀 더 효율적으로 지원서를 확인할 수 있다.

인터페이스는 이 예시의 양식에 해당한다. 작성된 지원서는 다르지만 양식은 동일한 것과 같이 구현되는 클래스와 메서드는 다르지만 인터페이스에 의해 기본 틀은 동일하게 되는 것이다.


## 인터페이스의 장점

### 정형화된 개발이 가능하고, 유지보수가 용이해진다.

한 개발자가 기능을 구현한 후에 담당자가 바뀌는 경우, 유지보수를 하기 위해 해당 기능이 구현된 코드를 찾아봐야한다. 소규모 프로젝트는 그나마 찾는 시간에 적게 걸리지만 대규모 프로젝트의 경우에는 시간이 오래 걸리고 찾기 어려울 수 있다. 특히 대기업에서 진행하는 경우, 개발자와 운영자가 다르기 때문에 코드를 파악하는데도 시간이 걸릴 수 있다.

이 경우에 interface를 사용하여 동일한 양식을 사용하는 경우 interface만 알면 어디에 구현했는지 빠르게 파악 할 수 있기 때문에 유지보수가 용이해진다.

예를 들어서 insert API 구현할 때, 다음과 같이 다양한 메서드 명을 가진다면 운영자가 확인하기 어려워진다.

```java
class A {
    public void insert() {
        
    }
}

class B {
    public void add() {
        
    }
}
```

이러한 경우 interface를 사용하여 다음과 같이 동일하게 만들어 준다면 운영자는 insert() 메서드만 확인하면 된다.
```java

class A implements MyAPI {

    @Override
    public void insert() {
        
    }
}

class B implements MyAPI {

    @Override
    public void insert() {
        
    }
}
```

### 유연한 프로그래밍이 가능하다.(코드 종속성이 낮아짐)

(멍토님 블로그 참고)
예를 들어서,

자동차의 제한속도를 준수하며 속도 값을 돌려주는 프로그램을 만들려고 한다.

한국에서 제한 속도를 150km/h로 준다고 가정하면 다음과 같이 구현할 수 있다.
```java

public class Car {

    private static final int KOREA_LIMIT_SPEED = 150;

    public int movedCarSpeed(int speed) {
        return Math.min(KOREA_LIMIT_SPEED, speed);
    }
}

class Test {
    public static void main(String[] args) {
        Car car = new Car();
        System.out.println(car.movedCarSpeed(80)); // 80
        System.out.println(car.movedCarSpeed(180)); // 150
    }
}

```

150km/h의 제한속도를 넘으면 150km/h의 속도를 유지하도록 한다.

이 회사가 외국에 자동차를 수출하는 경우 각 나라마다 다른 제한속도를 적용해야 한다.

나라가 추가될 때마다 각 나라에 대한 클래스를 추가하면 유연하지 못한 프로그래밍 방식이 된다.

이를 해결하기 위해 Interface를 사용한다.

```java

interface InterfaceCarSpeed {

    int speed(int speed);
}

class KoreaCarSpeed implements InterfaceCarSpeed {

    private static final int MAX_SPEED = 120;

    @Override
    public int speed(int speed) {
        return Math.min(MAX_SPEED, speed);
    }
}

class ChinaCarSpeed implements InterfaceCarSpeed {

    private static final int MAX_SPEED = 140;

    @Override
    public int speed(int speed) {
        return Math.min(MAX_SPEED, speed);
    }
}

class JapanCarSpeed implements InterfaceCarSpeed {

    private static final int MAX_SPEED = 100;

    @Override
    public int speed(int speed) {
        return Math.min(MAX_SPEED, speed);
    }
}

class Car {

    private final InterfaceCarSpeed carSpeed;

    public Car(final InterfaceCarSpeed interfaceCarSpeed) {
        this.carSpeed = interfaceCarSpeed;
    }

    public int movedCarSpeed(int speed) {
        return carSpeed.speed(speed);
    }
}

class Test {
    public static void main(String[] args) {
        ChinaCarSpeed speeds = new ChinaCarSpeed();
        System.out.println(speeds.speed(150)); // 140
        Car car = new Car(speed -> 120);
        System.out.println(car.movedCarSpeed(100)); // 120
        System.out.println(car.movedCarSpeed(150)); //120
        Car chinaCar = new Car(speeds);
        System.out.println(chinaCar.movedCarSpeed(50)); // 50
        System.out.println(chinaCar.movedCarSpeed(180)); // 140
    }
}
```

인터페이스를 사용함으로서 각 나라의 제한속도에 맞게 속도를 돌려주는 class를 구현할 수 있게 되었고,

자동차의 속도를 돌려주는 class Car는 공통으로 사용할 수 있게되었다.

<br>
인터페이스의 장점을 정리하면 다음과 같다.

**=> 정형화된 개발이 가능하다.**

프로젝트의 모든 insert기능을 insert() 메서드에서 구현한다.
**(추가적으로 개발자는 method 명을 고민하지 않아도 된다.)**


**=> 유지보수에 용이해진다.**

운영자는 insert 기능을 확인할 때 insert() 메서드만 찾아보면 된다.


**=> 클래스마다 독립적인 프로그래밍이 가능하다.(코드의 종속성이 낮아진다.)**

insert 기능을 각 클래스에서 서로 다른 조건으로 구현할 수 있다.





<br>
<br>
<br>

참고:

https://mungto.tistory.com/314