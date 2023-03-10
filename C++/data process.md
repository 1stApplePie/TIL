# 데이터 처리
객체 지향 프로그래밍(OOP)의 진수는 사용자가 데이터형을 스스로 설계하고 확장할 수 있다는 데에 있다. C++에 내장된 데이터형에는 기본형과 복합형이 있다. 오늘은 기본형에 대해서만 알아본다. 기본형에는 정수를 표현할 수 있는 정수형과, 소수부가 있는 수를 표현할 수 있는 부동 소수점형이 있다. 언뜻 들으면 두 가지 데이터형만 있는것처럼 들리지만, 하나의 정수형과 하나의 부동 소수점형만 가지고는 모든 프로그래밍 상황에 대처할 수 없기 때문에 필요에 따라 골라 쓸 수 있는 여러 가지 변형 데이터형이 이들을 기초로 하여 만들어져 있다.  
  
* ## 간단한 변수
컴퓨터에 정보를 저장하려면 다음 세 가지 사항을 알아야 한다.
* 어디에 저장되는가?
* 어떤 값이 저장되는가?
* 어떤 종류의 정보인가?
이제까지 변수 선언으로 정보를 저장해왔다. 변수 선언에 나오는 데이터형은 정보의 종류를 나타내고, 변수 이름은 그 값을 기호로 나타낸 것이다. 다음과 같은 구문을 사용한다고 가정해보자.
```
int braincount;
braincount = 5;
```
이 구문은 하나의 정수를 저장할 것이며, braincount라는 이름이 그 정수의 값, 즉 5를 나타낸다고 프로그램에게 알려준다. 이 구문만 보고는 그 값이 메모리의 어디에 저장되는지 알 수 없다. 그러나 프로그램은 그 위치를 추적할 수 있다. 사용자도 &연산자를 사용하면 braincount의 메모리 주소를 알아낼 수 있다.  
* ### 변수 이름
C++에서는 의미를 쉽게 알 수 있는 변수 이름을 사용할 것을 권장한다. 어떤 변수가 여행 비용을 나타낸다면, 변수 이름을 x나 cot로 하지말고, cost_of_trip 또는 costOfTrip으로 해야한다. C++에서 변수 이름을 지을 때에는 다음과 같은 간단한 규칙을 따라야 한다.
* 변수 이름에는 영문자, 숫자, 밑줄 문자만을 사용할 수 있다.
* 숫자를 변수 이름의 첫 문자로 사용할 수 없다.
* 변수 이름에서 대문자와 소문자는 구별된다.
* C++의 키워드는 변수 이름으로 사용할 수 없다.
* 두 개의 밑줄 문자로 시작하는 이름이나, 밑줄 문자와 대문자로 시작하는 이름은 그것을 사용하는 컴파일러와 리소스가 사용하기로 예약이 되어있다. 하나의 밑줄 문자로 시작하는 이름은, 그것을 사용하는 컴파일러와 리소스가 전역 식별자(global identifier)로 사용하기로 예약되어 있다.
* 변수 이름의 길이는 제한이 없으며, 변수 이름에 쓰인 모든 문자들이 유효하다. 그러나, 어떤 플랫폼은 고유의 길이 제한이 있다.  
  
뒤에서 두 번째 규칙은 __time_stop 또는 _Dount같은 이름을 사용해도 컴파일러 에러가 발생하지 않고, 정의되지 않는 이상한 동작을 일으킨다는 뜻에서 앞의 네 가지 규칙과는 성격이 조금 다르다. 컴파일러 에러가 발생하지 않는 이유는 이름은 적법하지만 컴파일러가 사용하기로 예약되어 있기 때문이다. 전역 이름에 사용된 하나의 밑줄 문자는 그 이름이 전역적으로 선언된 것임을 알려준다.  
  
다음은 C++의 변수 이름으로 맞는 것과 틀리는 것의 예이다.
```
int poodle;         // 맞다
int Poodle;         // 맞다. poodle과 구별된다
int POODLE;         // 맞다. poodle과 더 확실히 구별된다.
Int terrier;        // 틀리다. Int가 아니라 int가 맞다.
int my_stars3;      // 맞다
int _Mystarts3;     // 맞다. 예약 _밑줄문자로 시작하므로
int 4ever;          // 틀리다. 숫자로 시작할 수 없다.
int double;         // 틀리다. double은 C++ 키워드이므로
int begin;          // 맞다. begin은 Pascal 키워드 이므로 상관없다.
int __fools;        // 맞다. 예약 두 개의 밑줄 문자로 시작하므로
int the_very_best_variable_i_can_be_version_112;    // 맞다
int honky-tonk;     // 틀리다. 하이픈을 사용할 수 없다
```
두 개 이상의 단어를 결합하여 변수 이름을 지을 때에는 my_options와 같이 밑줄로 단어를 구분하거나, myEyeTooth와 같이 첫 단어를 제외하고 각 단어들의 첫 문자를 대문자로 쓰는것이 관례이다.
* ### 정수형
정수는 소수부가 없는 수를 뜻한다. 그런데 컴퓨터의 메모리 용량에는 한계가 있으므로 무한하게 많은 정수를 컴퓨터로 모두 나타낼 수는 없다. 따라서 컴퓨터 언어는 정수들의 부분 집합만을 나타낼 수 있다. C++는 여러 가지 정수형을 제공한다. 이것은 프로그램이 요구하는 특정 상황에 가장 알맞은 정수형을 골라 사용할 수 있도록 하기 위해서이다. 
 
C++의 여러 정수형들은 서로 다른 크기의 메모리를 사용하여 정수를 저장한다. 메모리 블록이 클수록 나타낼 수 있는 정수값의 범위가 크다. signed 데이터형은 양수값과 음수값을 모두 나타낼 수 있으나, unsigned 데이터형은 양수값만 나타낼 수 있다. 정수를 저장하는 데 사용되는 메모리의 크기를 폭(width)이라 한다. 메모리 크기가 클수록 폭이 넓다. C++의 기본 정수형을 크기 순서로 나열하면  
```
char < short < int < long < longlong(C++ 11)
```
의 순서이다. 이 기본형들에 대해 signed형과 unsigned형이 각각 따로 존재한다. 그러므로 모두 합하여 여덟 가지의 기본형이 있는 셈이다. 이제 이 정수형들을 자세히 살펴보자

* ## short, int ,long, long long
컴퓨터의 메모리는 비트라는 단위로 이루어진다. C++에서 short, int, long은 정수를 저장하는데 사용하는 비트 수가 다르다. 따라서 이들은 각각 폭이 다른 세 가지 정수 범위를 나타낼 수 있다. 예를 들면 short형은 언제나 16비트, int형은 언제나 32비트, 이런 식으로 모든 C++에서 동일한 데이터형이 동일한 폭을 갖는다면 매우 편리할 것이다. 그러나 세상ㅇ은 말처럼 그렇게 단순하지가 않다. 모든 컴퓨터를 만족시킬 수 있는 탁월한 선택은 없다. 그래서 C++는 이 데이터 형들의 최소 크기만을 정하여 보다 융통성 있는 표준을 제공한다.
* short형은 최소한 16비트 폭을 가진다.
* int형은 최소한 short만큼은 크다.
* long형은 최소한 32비트 폭을 가지며, 최소한 int만큼은 크다.
* long long형은 최소한 64비트 폭을 가지며, 최소한 long만큼은 크다.  
기존 int형 변수를 선언했던것과 같이 다른 데이터형들의 변수도 선언이 가능하다.  
```
short score;        // short형의 정수형 변수를 만든다.
int temperature;    // int형의 정수형 변수를 만든다.
long position;      // long형의 정수형 변수를 만든다.
```
여기서 short는 short int를 줄인것이고, long은 long int를 줄인 것이다. 대부분의 프로그래머가 이와 같이 줄인 표현을 사용한다.  
  
사용하는 C++시스템의 정수 크기가 얼마인지 알고 싶으면 첫 번째 방법은 크기를 알아내는 도구인 
```
sizeof
```
연산자를 사용하여 알 수 있다. sizeof 연산자는 변수나 데이터형의 크기를 바이트 단위로 리턴한다.  
  
두 번째 방법은 여러 가지 정수형들의 범위에 대한 정보가 들어 있는 climits헤더 파일을 열어 보는 것이다. 이 파일은 여러 정수형들의 서로 다른 한계값을 기호 이름으로 정의하고 있다. 예를 들면 int형의 최대 값을 INT_MAX, char형의 비트 수를 CHAR_BIT로 정의하고 있다. Listing 3.1은 이것을 사용하는 방법을 보여준다.
```
// Listing 3.1
// limits.cpp
#include <iostream>
#include <climits>  // 구식 C++에는 limits.h를 사용한다.
int main()
{
    using namespace std;
    int n_int = INT_MAX;    // n_int를 int형의 최대값으로 초기화
    short n_short = SHRT_MAX;   // limits.h 파일에 정의된 기호 상수
    long n_long = LONG_MAX;
    long long n_llong = LLONG_MAX;
    // sizeof 연산자는 데이터형이나 변수의 크기를 알아낸다.
    cout << "int는 " << sizeof (int) << " 바이트이다." << endl;
    cout << "short는 " << sizeof n_short << " 바이트이다." << endl;
    cout << "long는 " << sizeof n_long << " 바이트이다." << endl;
    cout << "long long는 " << sizeof n_llong << " 바이트이다." << endl;
    cout << endl;
    cout << "최대값: " << endl;
    cout << "int: " << n_int << endl;
    cout << "short: " << n_short << endl;
    cout << "long: " << n_long << endl;
    cout << "long long: " << n_llong << endl; << endl;
    cout <<"int의 최솟값 = " << INT_MIN << endl;
    cout << "바이트 당 비트 수 = " << CHAR_BIT << endl;
    return 0;
}
```
다음은 Listing 3.1의 출력 예시이다.
```
int는 4 바이트이다.
short는 2 바이트이다.
long는 4 바이트이다.
long long는 8 바이트이다.
최대값:
int: 2147483647
short: 23767
long: 2147483647
long long: 9223372036854775807
int의 최솟값 = -2147483648
바이트 당 비트 수 = 8
```

* ### sizeof 연산자와 climits 헤더 파일
sizeof 연산자는 우리가 사용한 기본 시스템에서 int형이 4바이트라고 보고한다. sizeof 연산자는 데이터형 이름이나 변수 이름에 모두 사용할 수 있다. int와 같은 데이터형 이름에 sizeof 연산자를 사용할 때에는 괄호를 사용해야 하며, n_short와 같은 변수 이름에 사용할 때에는 괄호가 없어도 상관없다.
```
cout << "int는 " << sizeof (int) << " 바이트이다." << endl;
cout << "short는 " << sizeof n_short << " 바이트이다." << endl;
```
climits 헤더 파일은 데이터형의 한계값을 나타내기 위해 기호 상수를 사용한다.

* ### 초기화
초기화는 선언과 대입을 하나로 조합한다. 예를 들어, 다음과 같은 구문은
```
int n_int = INT_MAX;
```
n_int 를 int형 변수로 선언하고, 그 변수에 int형의 최대값을 대입한다. 또는 255와 같은 상수를 사용할 수도 있다. 이때 이와 같은 기호 상수가 아닌 일반 상수로도 초기화할 수 있다. 또는 앞에서 정의한 변수로도 초기화할 수 있다. 심지어 프로그램 실행이 그 선언에 접근할 때 수식 안의 값들이 모두 알려진다면, 수식으로도 초기화할 수 있다.
```
int uncles = 5;                     // uncles를 5로 초기화
int aunts = uncles;                 // aunts를 5로 초기화
int chairs = aunts + uncles + 4;    // chairs를 14로 초기화
```
맨 앞의 uncles에 대한 선언을 맨 뒤로 옮기면 나머지 두 개의 초기화는 실패한다. 그 이유는 프로그램이 aunts와 chairs를 초기화하려고 시도할 때 uncles의 값을 아직 알 수 없기 때문이다.  
  
앞에서 보여준 초기화 문법은 C언어에서 유래한 것이다. C++는 C와는 다른 새로운 초기화 문법을 가지고 있다.
```
int owls = 101; // 전통적인 C스타일의 초기화 문법
int wrens(432); // C++의 새로운 초기화 문법, wrens를 432로 초기화
```
변수가 어떤 초기값을 가져야 하는지 분명히 알고 있다면 반드시 초기화하라. 변수 선언과 값 대입을 분리하면 일시적으로 변수의 값이 미확정 상태가 된다.
```
short year;     // 변수 year의 값이 미확정 상태
year = 1492;    // 변수 year의 값이 1492로 확정된 상태
```
변수를 선언할 때 아예 값을 대입하여 초기화까지 하면, 나중에 잊어버리고 변수에 값을 대입하지 않는 실수를 예방할 수 있다.

* ## unsigned 형
앞에서 설명한 세 가지 기본 정수형은 음의 정수값을 저장할 수 없는 unsigned변형을 하나씩 가지고 있다. unsigned형을 사용하면 그 변수에 저장할 수 있는 최대값을 늘릴 수 있다. 예를 들어 short형이 -32768에서 +32767까지의 범위를 갖는다면, unsigned short는 0부터 65535까지의 범위를 갖는다. 물론 unsigned형은 인구 수, 낱알 수, 웃는 얼굴 표정 수와 같이 결코 음수가 될 수 없는 양을 나타낼 때에만 사용해야 한다. 기본 정수형들의 unsigned형 변수를 선언하려면 unsigned 키워드를 앞에 븥여서 선언하면 된다.
```
unsigned short change;      // unsigned short형
unsigned int rovert;        // unsigned int형
unsigned quarterback;       // unsigned int형
unsigned long gone;         // unsigned long형
unsigned long long lang_lang // unsigned long long형
```
Listing 3.2는 unsigned형을 사용하는 방법을 설명한다. 또한 프로그램이 정수형의 범위를 벗어나려고 시도하면 어떤 일이 벌어지는지도 설명한다. 마지막으로 #define 전처리 지시문을 보여 준다.
```
// Listing 3.2
// exceed.cpp
#include <iostream>
#define ZERO 0      // 값 0으로 대체될 기호 상수 ZERO를 정의한다.
#include <climits>  // INT_MAX가 int형의 최대값으로 정의되어 있다.
int main()
{
    using namespace std;
    short Dohee = SHRT_MAX;     // 변수를 최대값으로 초기화
    unsigned short Insuk = Dohee;   // Dohee가 정의되어 있으므로 맞다.

    cout << ""도희 계좌에는 " << Dohee << "원이 들어있고, ";
    cout << "인숙이의 계좌에도 " << Insuk << "원이 들어있다."<< endl;
    cout << "각각의 계좌에 1원씩 입금한다." << endl << "이제 ";
    Dohee = Dohee + 1;
    Insuk = Insuk + 1;
    cout << "도희 잔고는 " << Dohee << "원이 되었고, ";
    cout << "인숙이의 잔고는 " << Insuk << "원이 되었다." << endl;
    cout << "이럴 수가! 도희가 나 몰래 대출을 했나?" << endl;
    Dohee = ZERO;
    Insuk = ZERO;
    cout << "도희 계좌에는 " << Dohee << "원이 들어있고, ";
    cout << "인숙이의 계좌에도 " << Insuk << "원이 들어있다." << endl;
    cout << " 각각의 계좌에서 1원씩 인출한다." << endl << "이제";
    Dohee = Dohee - 1;
    Insuk = Insuk - 1;
    cout << "도희 잔고는 " << Dohee << "원이 되었고, ";
    cout << "인숙이의 잔고는 " << Insuk << "원이 되었다." << endl;
    cout << "이럴 수가! 인숙이가 복권에 당첨되었나?" << endl;
    return 0;
}
```

이 프로그램은 short형 변수(Dohee)와 unsigned short형 변수(Insuk)를  short형의 최대값인 32767로 설정한다. 그러고 나서 각 변수에 1씩 더한다. 이 경우 Insuk에는 아무 문제도 발생하지 않는다.  
  
그 이유는 32767에 1을 더해도 unsigned short형의 최대값인 65535보다 여전히 작기 때문이다. 그러나 short형인 Dohee는 32767에서 -32768로 갑자기 넘어간다. 마찬가지로 Dohee와 Insuk모두 0으로 설정한 후, Dohee에서 1을 빼는 것은 문제가 발생하지 않지만, unsigned short형인 Insuk에서 1을 빼면 0에서 65535로 갑자기 넘어간다. 이러한 동작을 우리는 자동차 미터기에서 흔히 볼 수 있다. 즉, 표현할 수 있는 한계를 벗어나려면 그 표현 범위의 반대편에서부터 다시 시작한다.  
  
C++는 표현 한계값을 벗어날 때(오버플로와 언더플로가 발생할 때) 부호 없는 unsigned 정수형의 경우에 한상 이와 같이 동작한다. 부호 있는 signed 정수형의 경우에는 항상 이와 같이 동작한다고 보장할 수 없다. 그러나 현재 대부분의 C++는 이와 같은 방식으로 동작하고 있다.

* ## 어느 정수형을 사용할 것인가?
일반적으로 int형은 컴퓨터에서 가장 효율적인 크기로 설정된다. 그러므로 어쩔 수 없이 다른 정수형을 사용해야 하는 경우가 아니라면, 가급적이면 int형을 사용해야 한다.  
  
다른 정수형들은 왜 사용하는지 살펴보자. 문서에 포함되어 있는 단어 수와 같이 결코 으수가 될 수 없는 수를 나타낼 때에는 부호 없는 unsigned 정수형을 사용한다. 부호 없는 정수형의 사용은 signed값보다 더 큰 값을 나타낼 수 있다.  
  
숫자의 크기에 따라서는 short << int << long << long long 의 적절한 사용으로 프로그램의 오작동을 예방할 수 있다.

* ## 정수형 상수
정수형 상수는 212, 1432와 같이 프로그램에 직접 써 넣는 정수를 말한다. C에서와 마찬가지로, C++에서도 세 가지 방법
* 일상생활에서 사용하는 10진수
* 구식 Unix가 사용하던 8진수
* 하드웨어 전문가가 좋아하는 16진수  

로 정수형 상수를 프로그램에 직접 넣을 수 있다.  
C++에서는 정수형 상수의 처음 하나의 숫자 또는 처음 두 개의 문자가 진수를 의미한다. 처음 숫자가 1에서 9이면 그 수는 10진수를 나타낸다. 처음 숫자가 0이고 두 번째 숫자가 1에서 7이면 그 수는 8진수를 나타낸다. 따라서 042는 8진 정수형 상수이며, 10진수로 34이다.
그리고 처음 두 개의 문자가 0x 또는 0X이면 16진수를 나타낸다. Listing 3.3은 세 가지 진법을 어떻게 사용하는지 설명한다.
```
// Listing 3.3
// hexoct1.cpp
#include <iostream>
int main()
{
    using namespace std;
    int chest = 42; // 10진 정수형 상수
    int waist = 0x42;   // 16진 정수형 상수
    int inseam = 042;   // 8진 정수형 상수

    cout << "가슴 둘레: " << chest << endl;
    cout << "허리 둘레: " << waist << endl;
    cout << "인심 길이: " << inseam << endl;
    return 0;
}
```
정수가 프로그램 안에서 어떤 진법으로 표현되었느냐와는 상관없이 기본적으로 cout은 10진수로 출력한다.  
  
어떤 정수값을 16진수나 8진수 형태로 출력하려면 cout의 특별한 기능을 사용해야 한다. iostream 헤더 파일은 새로운 행을 시작하라는 메시지를 cout에 전달하는 endl 조정자를 제공한다. 이와 비슷하게, iostream 헤더 파일은 정수를 10진수, 16진수, 8진수로 각각 디스플레이 하라는 메시지를 cout에 전달하는 dec, hex, oct 조정자를 제공한다. Listing 3.4는 10진수 42를 세 가지 형태로 디스플레이 하기 위해 hex와 oct를 사용한다.
```
// Listing 3.4
// hexoct2.cpp
#include <iostream>
using namespace std;
int main()
{
    using namespace std;
    int chest = 42;
    int waist = 42;
    int inseam = 42;

    cout << "가슴 둘레: " << chest << "(10진수)" << endl;
    cout << hex;    // 진법을 바꾸는 조정자
    cout << "허리 둘레: " << waist << "(16진수)" << endl;
    cout << oct;    // 진법을 바꾸는 조정자
    cout << "인심 길이: " << inseam << "(8진수)" << endl;
    return 0;
}
```
* ## C++가 상수의 데이터 형을 결정하는 방법
프로그램에서 선언이 하는 역할은 변수의 데이터형을 C++ 컴파일러에게 알려 주는 것이다. 그렇다면 정수형 상수의 경우에는 어떻게 될까? 다음과 같이 프로그램에서 어떤 정수를 상수로 표현한다고 가정해보자.
```
cout << "Year = " << 1453 << endl;
```
프로그램은 1453을 int 형을 저장할까, long형으로 저장할까? 아니면 다른 정수형으로 저장할까? C++는 특별한 이유가 없다면 정수형 상수를 모두 int형으로 저장한다. 그러나 특정 데이터형을 의미하는 접미어를 상수에 붙였을 때와, 값이 너무 커서 int형으로 저장할 수 없을 때에는 그렇지 않다.  
  
먼저 접미어에 대해 살펴보자. 접미어는 상수의 끝에 붙는 문자로서 그 상수의 데이터형을 나타낸다. 1이나 L은 long형을 의미하고, u나 U는 unsigned int형을 의미한다. ul은 unsigned long을 의미한다.  
  
다음은 크기를 살펴보자. C++는 16진 정수나 8진 정수에 적용하는 규칙과는 약간 다른 규칙을 10진 정수에 적용하고 있다. 접미어가 없는 10진 정수는 int, long, long long형 중에서 크기가 가장 작은 것으로 나타낸다. 예를 들면, 16비트 int형과 32비트 long형을 사용하는 시스템에서, 20000은 int형으로, 40000은 long형으로, 30000000000은 longlong형으로 나타낸다. 또한, 접미어가 없는 16진 정수나 8진 정수는 데이터형 중에서 크기가 작은 것으로 나타낸다.
  
* ## char형: 문자와 작은 정수
이제 마지막으로 남은 정수형인 char형에 대해 살펴보자. char형은 이름에서도 알 수 있듯이, 문자와 숫자를 저장하기 위한 것이다. 컴퓨터에서 수를 저장하는 것은 그다지 어려운 일이 아니지만 문자를 저장하는 것은 이와는 다른 문제이다. 프로그래밍 언어들은 문자를 수치 코드로 나타냄으로써 이 문제를 해결하고 있다. 그러므로 char형은 실제로 또 하나의 정수형이다. 컴퓨터 시스템에서 사용하는 문자와 숫자, 구두점과 같은 기본적인 기호들은 모두 char형으로 나타낼 수 있다. 대부분의 컴퓨터 시스템들은 256개보다 적은 개수의 문자들을 지원한다. 이러한 문자들은 1바이트만으로 충분히 나타낼 수 있다. 그러므로 char형 문자들을 처리하는데 사용할 수 있고, short형보다 작은 범위의 정수를 나타내는데 사용할 수도 있다. Listing 3.5를 통해 char형에 대해 알아보자.
```
// Listing 3.5
// chartype.cpp
#include <iostream>
int main()
{
    using namespace std;
    char ch;

    cout << "원하는 문자 하나를 입력하시오: " << endl;
    cin >> ch;
    cout << "감사합니다. ";
    cout << "당신이 입력한 문자는 " << ch << "입니다." << endl;
    return 0;
}
```
여기서 우리가 주목할 것은 입력할 때 문자 M에 해당하는 코드인 77을 입력하지 않고 문자 M자체를 입력한다는 것이다. 출력 또한 77이 아닌 M으로 출력된다.  
다음 예제는 문자를 화면에 출력하는 cout.put() 함수의 소개이다.
```
// Listing 3.6
// morechar.cpp
#include <iostream>
int main()
{
    using namespace std;
    char ch = 'M'   // M에 해당하는 ASCII 코드를 char형 변수 ch에 대입
    int i = ch;
    cout << ch << "의 ASCII 코드는" << i << "입니다." << endl;

    cout << " 이 문자 코드에 1을 더해 보겠습니다." << endl;
    ch = ch + 1;
    i = ch;
    cout << ch << "의 ASCII 코드는 " << i << "입니다." << endl;

    // cout.put() 멤버 함수를 사용하여 char형 변수 ch를 출력한다.
    cout << "cout.put(ch)를 사용하여 char형 변수 ch를 화면에 출력: ";
    cout.put(ch);

    // cout.put()을 사용하여 문자 상수를 출력한다.
    cout.put('!');

    cout << endl << "종료" << endl;
    return 0;
}
```
Listing 3.6 프로그램에서 'M'이라는 표기는 문자 M에 해당하는 수치 코드를 의미한다. 그러므로 char형 변수 ch를 'M'으로 초기화하면 값 77이 ch에 대입된다. 프로그램은 동일한 값을 int형 변수 i에도 대입한다. 따라서 ch와 i에는 동일한 값 77이 저장된다. 그러고 나서 cout은 ch를 M으로 출력하고, i를 77로 출력한다. 이것은 잘 짜여진 객체의 능력을 보여 주는 또 하나의 예이다.

* ### 멤버 함수: cout.put()
cout.put()은 무엇일까? 그리고 그것의 이름에는 왜 마침표가 들어있을까?  
cout.put()은 C++ 객체 지향 프로그래밍에서 중요한 개념인 멤버 함수를 설명하는 첫 번째 예이다. 클래스는 데이터 형식과 그 데이터를 다루는 방법을 정의해 놓은 것이라고 앞에서 설명했다. 멤버 함수는 클래스에 속하고, 클래스의 데이털르 다루는 방법을 정의한다. 예를 들어, ostream클래스는 문자를 출력하도록 설계된 put()함수를 가지고 있다.  
  
멤버 함수는 그 클래스의 특정 객체를 통해서만 사용할 수 있다. 이 예제에서는 cout객체를 통해 put()이라는 멤버 함수를 사용한다. cout과 같은 객체를 통해 멤버 함수를 사용하려면 마침표로 객체 이름(cout)과 함수 이름(put())을 서로 연결해야 한다. 이 마침표를 멤버 연산자(emebership operator)라고 부른다. cout.put()이 나타내는 의미는 클래스 객체인 cout을 통해 클래스 멤버 함수인 put() 을 사용하겠다는 뜻이다.  
cout.put()멤버 함수는 << 연산자를 사용하여 문자를 출력하는 것에 대한 대안이다.

* ### ASCII
ASCII코드에 관해서는 python에서도 공부한 바 있다. 따라서 예제 하나만 보고 넘어가도록 하자.
```
// Listing 3.7
// bondini.cpp
#include <iostream>
int main()
{
    using namespace std;
    cout << "\a암호명  \"화려한외출\"작전이 방금 개시되었습니다.\n";
    cout << "8자리 비밀번호를 입력하십시오:________\b\b\b\b\b\b\b\b";
    long code;
    cin >> code;
    cout << "\a입력하신 비밀번호는 " << code << "입니다.\n";
    cout << "\a비밀번호가 맞습니다! Z3 계획을 진행하십시오!\n";
    return 0;
}
``` 

* ### 유니버셜 네임 코드
C++ 시스템은 소스 코드를 작성하는 데 사용할 수 있는 기본적인 소스 문자 세트를 지원한다. 소스 문자 세트는 미국 표준 자판 위에 있는 문자(대문자와 소문자)와 숫자, (또는 =와 같은 기호, 그리고 개행이나 빈칸 문자와 같은 분리자들로 이루어진다. 또한 기본적인 실행 문자 세트도 지원한다. 여기에는 백스페이스나 경보 문자와 같은 특수 용도의 문자들이 추가된다. 또한 C++ 표준은 C++ 시스템이 확장 실행 문자 세트를 제공하는 것을 허용한다. 더불어, 글자 자격을 갖춘 그러한 부가 문자들을 식별자 이름의 일부로 사용하는 것도 허용한다. C++는 특정 키보드와는 무관한 국제 문자들을 표현하는 매커니즘도 가지고 있다. 그것이 유니버셜 네임 코드(universal character names)의 사용이다.

* ### signed char형과 unsigned char형
int형과는 달리, char형은 signed형이나 unsigned형으로 미리 정해져 있지 않다. 그것은 C++ 시스템 개발자가 하드웨어의 특성에 맞추어 알맞은 char형을 정할 수 있도록 하기 위한 배려이다. 그러나 char형이 어느 특별한 한 가지 행동만을 보여야 한다면, signed char형 또는 unsigned char형을 사용하여 그 행동을 명시적으로 제한할 수 있다.
```
char fodo;      //signed형 또는 unsigned형
unsigned char bar   // 명백히 unsigned형
signed char snark;  // 명백히 signed형
```
이러한 구별은 char형으로 수를 나타내고자 할 때 특히 중요하다. unsigned char형은 0에서 255까지의 범위를 나타낼 수 있고, unsigned char형은 -128부터 127까지의 범위를 나타낼 수 있다.  
* ### 확장 char형: wchar_t
때로는 프로그램이 1바이트로 표현할 수 없는 문자 세트를 처리해야 하는 경우도 있다.(ex.일본어, 중국어, 한국어 문자 세트)C++는 이것을 두 가지 방법으로 처리한다. 첫째, 확장 문자 세트가 시스템의 기본 문자 세트이면, 컴파일러 개발업체가 char형을 처음부터 2바이트 또는 그 이상으로 만드는 것이다. 둘째, 기본 문자 세트와 확장 문자 세트를 동시에 지원하는 것이다. 즉, 보통의 8비트 char형으로 기본 문자 세트를 나타내고, wchar_t형(wide character type)으로 확장 문자 세트를 나타내는 것이다. wchar_t형은 시스템에서 사용되는 가장 큰 확장 문자 세트를 나타낼 수 있을 만큼의 충분한 비트 폭을 가진 정수형이다. wchar_t형은 기초 데이터형(underlying type)이라고 부르는 정수형과 동일한 크기와 부호 속성을 가진다.

## bool형
ANSI/ISO C++표준에는 bool이라는 새로운 데이터형이 추가되었다. 이는 python에서도 자주 다루었으므로 추가적으로 필요한 내용이 있다면 추후에 다루겠다.

# const 제한자
상수를 기호 이름으로 나타내면 그 상수가 무엇을 의미하는 것인지 금방 알 수 있다. 그리고 프로그램이 그 상수를 여러 곳에서 사용하고 있더라도, 상수의 값을 바꿀 필요가 있을 때 기호 이름이 정의된 부분만 살짝 바꾸면 모든 것이 해결된다.  
이 단원의 앞에서 다룬 #define보다 더 쉽게 기호상수를 다루는 법이 const키워드 사용이다. 예를 들어, 1년의 달 수를 기호 상수로 나타내고 싶다면, 프로그램에 다음과 행을 넣으면 된다.
```
const int MONTHS = 12;
```
이를 일반화 하면
```
const 데이터형 상수이름 = 값;
```
으로 나타낼 수 있으며, 다음의 예는 좋지 않은 예이다.
```
const int toes; // 이 시점에서 toesㅇ의 값은 미확정
toes = 10;  // 너무 늦은 초기화
```
const 상수는 선언할 때 값으로 초기화하지 않으면 변경할 수 없는 미확정값으로 남겨진다.  
C를 알고 있는 사용자는, 초기에 논의한 #define문으로도 충분하다고 주장할 것이다. 그러나 const를 사용하는 것이 더 좋다. 첫 번째 이유는 데이터형을 명시적으로 지정할 수 있다는 점이고, 두 번째 이유는 C++의 활동 범위 규칙(scoping rools)에 의해 그 정의를 특정 함수나 파일에서만 사용할 수 있도록 제한할 수 있다는 점이다.  
  
# 부동 소수점수
지금까지 우리는 C++의 정수형에 대해 살펴보았다. 이제 C++의 두 번째 기본 데이터형인 부동 소수점형에 대해 알아보자. 부동 소수점형은 0.56과 같이 소수부가 있는 수를 나타낼 수 있다. 또한 매우 큰 값들을 나타낼 수 있다.  
컴퓨터는 소수부가 있는 이러한 값을 두 부분으로 나누어 저장한다. 한 부분은 기본값을 나타내고, 다른 한 부분은 기본값을 키우거나 줄이는 스케일을 나타낸다. 두 수 34.1245, 34124.5가 있을 때, 이 두 수는 기본값은 같고 스케일만 다르다. 첫 번째 수는 기본값이 0.341245이고, 스케일이 100이다. 두 번째 수는 기본값이 0.341245이고 스케일이 100000이다. 소수점이 스케일에 따라 자리를 옮기기 때문에 이 데이터형을 부동 소수점형이라고 부른다. 2진수를 사용하는 것만 다를 뿐 C++도 부동 소수점수를 내부적으로 이와 같은 방식으로 나타낸다. C++에선느 스케일 인수가 10이 아닌 2이다. 사용자가 이렇게 내부적인 것 까지 알 필요는 없다.
* ## 부동 소수점수의 표기
C++가 부동 소수점수를 표기하는 방법은 두 가지이다. 그중 하나는 우리가 일상 생활에서 늘 사용하는 소수점 표기법을 그대로 사용하는 것이다.
```
12.34       // 부동 소수점수
939001.32   // 부동 소수점수
0.00023     // 부동 소수점수
8.0         // 부동 소수점수
```
8.0과 같이 소수부가 비록 0이라 할지라도 소수점이 있기 때문에 8.0은 정수형이 아닌 부동 소수점형으로 표현된다.  
C++가 부동 소수점수를 나타내는 두 번째 방법은 3.45E6과 같이 지수 표기를 사용하는 것이다. 3.45E6은 값 3.45dp 1,000,000을 곱하라는 뜻이다.

* ## 부동 소수점형
ANSI C와 마찬가지로, C++에는 float, double, long double의 세 가지 부동 소수점형이 있다. 이 데이터형들은 유효 숫자의 개수와 지수의 최소 혀용 범위가 다르다.  
C와 C++에서는 유효 숫자들을 저장하기 위해 float형은 최소한 32비트, double형은 최소 48비트, long double형은 최소 double형과 같은 크기를 요구한다. 이 세가지가 모두 같은 크기일 수도있다.
```
// 유효 숫자의 개수
#define DBL_DIG 15  // double형
#define FLE_DIG 6   // float형
#define LDBL_DIG 18 // long double형

// 가수를 표현하는데 사용되는 비트 수
#define DBL_MANT_DIG 53
#define FLT_MANT_DIG 24
#define LDBL_MANT_DIG 64

// 지수의 최대값과 최소값
#define DBL_MAX_10_EXP +308
#define FLT_MAX_10_EXP +38
#define LDBL_MAX_10_EXP +4932
#define DBL_MIN_10_EXP -307
#define FLT_MIN_10_EXP -37
#define LDBL_MIN_10_EXP -4931
```
Listing 3.8은 float형과 double형을 사용하여 부동 소수점수를 표현할 때 정빌도에서 얼마나 차이가 나는지 설명한다. 여기서 setf()라는 ostream메서드를 미리 한번 사용해본다. 이것은 프로그램이 큰 값을 출력할 때 지수표기를 사용하지 않고, 소수점 아래 6자리 까지 표시할 수 있도록 해 준다.
```
// Listing 3.8
// floatnum.cpp

#include <iostream>
int main()
{
    using namespace std;
    cout.setf(ios_base::fixed, ios_base::floatfield);   // 고정 소수점 형식으로 출력
    float tub = 10.0 / 3.0;  // 유효 숫자 6개
    double mint = 10.0 / 3.0;   // 유효 숫자 15개
    const float million = 1.0e6;;
    
    cout << "tub = " << tub;
    cout << ", a million tubs = " << million * tub;
    cout << ", \nten milltion tubs = ";
    cout << 10 * millions * tub << endl;

    cout << "mint = " << mint << "and a million mints = ";
    cout << million * mint << endl;
    return 0;
}
```
다음은 Listing 3.8프로그램의 실행 결과이다.
```
tub = 3.333333, a million tubs = 3333333.250000,
ten million tubs = 33333332.000000
mint = 3.333333 and a milltion mints = 3333333.333333
```

* ### 프로그램 분석
일반적으로 cout은 뒤에 붙은 0을 출력하지 않는ㄴ다. 즉, 3333333.250000을 3333333.25로 출력할 것이다. 그러나 cout.setf()를 호출하면 최소한 새 버전의 C++에서는 이러한 행동이 무시된다.  
Listing 3.8에서 주목할 것은 float형이 double형보다 정밀도가 얼마나 떨어지느냐이다. tub와 mint는 둘 다 10.0/3.0으로 초기화되고 있다. 이 값은 3.3333333333...으로 계속된다. 여기서 cout은 소수점 아래 6자리 까지 출력하므로, tub와 mint는 둘 다 거기까지는 정확하게 출력한다. 그러나 각각의 값에 백만을 곱한 후에 출력하면 7번째 3의 뒤부터 값이 달라진다. 이것으로부터 tub가 7개의 유효 숫자를 가진다고 말할 수 있다. double형 변수는 13번째 3까지 유효하므로 최소한 13개의 유효 숫자를 가진다고 말할 수 있다.  
* ## 부동 소수점형 상수
프로그램은 부동 소수점형 상수를 어떤 부동 소수점형으로 저장할까? 일반적인 부동 소수점형 상수는 기본적으로 double형으로 저장된다. 부동 소수점형 상수를 float형으로 저장하고 싶으면 f나 F를 접미어로, long double형으로 저장하고 싶으면 l이나 L을 접미어로 사용하라.
```
1.234f      // float형 상수
2.45E20F    // float형 상수
2.345324E28 // double형 상수
2.2L        // long double형 상수
```
* ## 부동 소수점수의 장단점
부동 소수점수는 정수에 비해 두 가지 장점을 가진다. 첫째, 정수와 정수 사이에 있는 값을 나타낼 수 있다. 둘째, 스케일을 사용하여 매우 큰 범위의 값을 나타낼 수 있다. 그러나 부동 소수점수 연산은 수치 연산 보조 프로세서(math coprocessor)가 없는 컴퓨터에서 정수 연산보다 연산 속도가 느리다. 또한 정밀도를 잃을 수 있다. Listing 3.9는 부동 소수점형의 정밀도 손실 문제를 보여주고 있다.
```
// Listing 3.9
// fltadd.cpp

#include <iostream>
int main()
{
    using namespace std;
    float a = 2.34E+22f;
    float b = a = 1.0f;

    cout << "a = " << a endl;
    cout << "b - a = " << b - a << endl;
    return 0;
}
```
Listing 3.9 프로그램은 어떤 수에 1을 더한 후 원래의 수를 뺀다. 예상되는 결과는 1이어야 한다. 그러나 실제 실행 결과는 다음과 같다.
```
a = 2.34e+022
b - a = 0
```
2.34E22가 소수점 위로 23개의 숫자를 가진 큰 수이기 때문에 문제가 발생한 것이다. 이 수에 1을 더하는 것은 23번째 숫자에 1을 더하는 것과 같다. float형은 처음 6개의 숫자 또는 7개의 숫자 까지만 나타낼 수 있으므로, 23번째 숫저에 1을 더하는 것은 아무런 효과도 갖지 못한다.

# C++ 산술 연산자
C++는 기본적인 계산 - 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지셈을 위해 다섯 가지 연산자를 제공한다. 이때 모든 연산자는 파이썬과 동일하다. 해당 내용은 예제 Listing 3.10만을 확인하고 넘어가도록 하자
```
// Listing 3.10
// arith.cpp

#include <iostream>
int main()
{
    using namespace std;
    float hats, heads;      // 고정 소수점 형식으로 출력

     cout.setf(ios_base::fixed, ios_base::floatfield);
     cout << "수를 하나 입력하십시오: ";
     cin >> hats;
     cout << "다른 수를 입력하십시오: ";
     cin >> heads;
     
     cout << "hats = " << hats << "; heads = " << heads << endl;
     cout << "hats + heads = " << hats + heads << endl;
     cout << "hats - heads = " << hats - heads << endl;
     cout << "hats * heads = " << hats * heads << endl;
     cout << "hats / heads = " << hats / heads << endl;
     return 0;
}
```
