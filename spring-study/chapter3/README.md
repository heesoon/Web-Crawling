Spring DI(Dependency Injection) and IoC(Inversion of Control)
=======================================================================================
이 장에서 정리해야 할 사항은 아래와 같은 것 같다.

* Dependency full, Contextualized Dependency Loopkup(CDL)
* DI (Dependency Injection)
      * 생성자 주입
      * 메소드 주입
* DI 세가지 방식
      * Based on Property
      * Based on XML
      * Based on Annotation

### 1. XML 기반 의존성 주입
---------------------------------------------------------------------------------------
chapter2-example2 예제가 XML 기반의 의존성 주입 방식으로 XML 파일에 의존성과 관련된 정보를 bean 테그를 통해서 모두 기술해야 한다.

### 2. Annotation 기반 의존성 주입
---------------------------------------------------------------------------------------
XML 파일에 bean 관련 정보를 기술하는 대신 의존성과 관련된 클래스들에 annotation을 선언하고
자동으로 의존성을 찾아서 의존성을 주입하도록 하는 예제이다.

* example1 : simple example
      * 의존성 주입 대상이 되는 클래스 위에 @Component, @Controller, @Repository, @Service 선언
      * 의존성 클래스 내의 주입 대상 (생성자, 메소드) @Autowired, @Inject, @Resource 선언
      * XML (applicationContext.xml)에 context:component-scan 테그 추가
