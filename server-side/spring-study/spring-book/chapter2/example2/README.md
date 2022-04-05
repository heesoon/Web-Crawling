Build Environments
=======================================================================================
빌드 및 실행은 Command 상에서 Gradle 명령어를 사용했고, 소스 편집은 Visual Studio Code를 사용함.

### 1. Gradle 환경 구성을 위한 초기 설정
---------------------------------------------------------------------------------------

빌드할 코드들을 아래 Directory 구조로 chapter2-example2 아래에 복사한다.
```
    └─src
        └─main
            ├─java
            │  └─com
            │      └─apress
            │          └─prospring5
            │              └─ch2
            │                  │  HelloWorldSpringDI.java
            │                  │
            │                  └─decoupled
            │                          HelloWorldMessageProvider.java
            │                          MessageProvider.java
            │                          MessageRenderer.java
            │                          StandardOutMessageRenderer.java
            │
            └─resources
                    applicationContext.xml
```

이 상태에서 gradle init 수행 (gradle project를 만들기 위함)
reference : https://spring.io/guides/gs/gradle/          
  
chapter2-example2에서 gradle init 수행
* 1:basic 선택 (아래)
```
        PS E:\github\java_spring\spring-study\chapter2-example2> gradle init

        Select type of project to generate:
          1: basic
          2: application
          3: library
          4: Gradle plugin
        Enter selection (default: basic) [1..4] 1
```
* 1: Groovy 선택

```
        Select build script DSL:
          1: Groovy
          2: Kotlin
        Enter selection (default: Groovy) [1..2] 1
```
* 그냥 enter함

```
        Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no] no
```
* 그냥 enter함

```
        Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no]
        Project name (default: chapter2-example2):
```

gradle 설정 파일들이 추가됨 (다른 추가 폴더들도 새로 생김)
```
    │  .gitattributes
    │  .gitignore
    │  build.gradle
    │  gradlew
    │  gradlew.bat
    │  settings.gradle
```
### 2. Gradle 설정
---------------------------------------------------------------------------------------
Gradle의 빌드 지시는 build.gradle 파일을 통해서 진행된다. build.gradle을 편집기로 아래와 같이 작성한다.
```
      //plugins {
      //  id 'java'
      //}

      apply plugin: 'java'
      //apply plugin: 'eclipse'
      apply plugin: 'application'
      mainClassName = 'com.apress.prospring5.ch2.HelloWorldSpringDI'

      group = 'com.example'
      version = '0.0.1-SNAPSHOT'
      sourceCompatibility = '11'

      repositories { 
          mavenCentral() 
      }

      dependencies {
          // https://mvnrepository.com/artifact/org.springframework/spring-context
          implementation group: 'org.springframework', name: 'spring-context', version: '5.3.17'
          // https://mvnrepository.com/artifact/org.springframework/spring-beans
          implementation group: 'org.springframework', name: 'spring-beans', version: '5.3.17'

      }

      jar {
          archiveBaseName = 'chapter2-example1'
          archiveVersion =  '0.1.0'
      }
```
* 자바 환경 설정을 위하여 (아래 코드 추가)
```
      apply plugin: 'java'
```
* 자바 실행 파일 설정
```
      apply plugin: 'application'
      mainClassName = 'com.apress.prospring5.ch2.HelloWorldSpringDI'
```
* 외부 라이블러리 불러올 장소 지정
```
      repositories { 
          mavenCentral() 
      }
```
* 필요한 라이블러리 지정 : ApplicationContext를 사용하기 위해서 spring-context 추가해 줌
```
      dependencies {
          // https://mvnrepository.com/artifact/org.springframework/spring-context
          implementation group: 'org.springframework', name: 'spring-context', version: '5.3.17'
          // https://mvnrepository.com/artifact/org.springframework/spring-beans
          implementation group: 'org.springframework', name: 'spring-beans', version: '5.3.17'

      }
```
* 최종 실행 환경 및 파일 지정
```
      jar {
          archiveBaseName = 'chapter2-example1'
          archiveVersion =  '0.1.0'
      }
```

### 3. Build with Gradle Wrapper
---------------------------------------------------------------------------------------
Gradle에서 권장하는 빌드 방법이고 현재 디바이스에 설치된 java나 gradle를 설치할 필요없으며, 환경 종속적이지 않은 빌드 환경을 제공한다.
Gradle Wrapper 없이 gradle run으로도 실행된다.

* gradle wrapper 환경 생성
```
      gradle wrapper --gradle-version 7.4.1
```

* gradle wrapper를 통한 project 빌드
```
      ./gradlew build
```

* Project (Application) 실행
```
      ./gradlew run
```

* 실행 결과 (Visual Studio Code Terminal)
```
      6 actionable tasks: 6 up-to-date
      PS E:\github\java_spring\spring-study\chapter2-example2> ./gradlew run  

      > Task :run
      Hello World!!

      BUILD SUCCESSFUL in 2s
      3 actionable tasks: 1 executed, 2 up-to-date
      PS E:\github\java_spring\spring-study\chapter2-example2>
```