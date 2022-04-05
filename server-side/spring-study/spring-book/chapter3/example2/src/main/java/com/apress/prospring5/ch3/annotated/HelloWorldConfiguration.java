package com.apress.prospring5.ch3.annotated;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class HelloWorldConfiguration {
    @Bean
    public MessageProvider provider() {
        return new HelloWorldMessageProvider();
    }

    @Bean
    public MessageRenderer renderer() {
        MessageRenderer renderer = new StandardOutMessageRenderer();
        renderer.setMessageProvider(provider());
        return renderer;
    }
}

/*
 * 위의 코드는 아래 코드로 더 간단하게 대체될 수 있다.
 * 
 * package com.apress.prospring5.ch3.annotated;
 * 
 * import org.springframework.context.annotation.ComponentScan;
 * import org.springframework.context.annotation.Configuration;
 * 
 * @ComponentScan(basePackages = { "com.apress.prospring5.ch3.annotated" })
 * 
 * @Configuration
 * public class HelloWorldConfiguration {
 * 
 * }
 */