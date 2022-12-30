package main;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

// import chap07.Calculator;
import chap07.RecCalculator;
import config.AppCtx;

public class MainAspect {
    public static void main(String[] args){
        AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(AppCtx.class);
        
        // Calculator cal = ctx.getBean("calculator", Calculator.class);
        // "calculator" 빈의 실제 타입은 Calculator를 상속한 프록시 타입이므로 RecCalculator로 타입 변환을 할 수 없음
        // @EnableAspectJAutoProxy(proxyTargetClass = true)를 이용하면 타입 변환 가능
        RecCalculator cal = ctx.getBean("calculator", RecCalculator.class);
        long fiveFact = cal.factorial(5);
        System.out.println("cal.factorial(5) = "+fiveFact);
        System.out.println(cal.getClass().getName());
        ctx.close();
    }
}
