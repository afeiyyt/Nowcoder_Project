package com.afeiyyt;

/**
 * Created by afeiyyt on 2019/5/7.
 */
public class Human extends Animal {
    private String country;

    public Human(String name, int age, String county) {
        super(name, age);
        this.country = county;
    }

    public void say() {
        System.out.println("This is " + getName() + " from " + country);
    }
}
