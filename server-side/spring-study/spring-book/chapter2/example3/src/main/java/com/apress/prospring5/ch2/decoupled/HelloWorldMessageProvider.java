package com.apress.prospring5.ch2.decoupled;

public class HelloWorldMessageProvider implements MessageProvider {

    public HelloWorldMessageProvider(){
        System.out.println(" --> HelloWorldMessageProvider() called");
    }

    @Override
    public String getMessage() {
        return "Hello World!";
    }
}
