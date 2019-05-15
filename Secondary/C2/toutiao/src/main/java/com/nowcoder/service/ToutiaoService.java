package com.nowcoder.service;

import org.springframework.stereotype.Service;

@Service //定义为service 可以在Controller中使用
public class ToutiaoService {
    public String say() {
        return "This is from  ToutiaoService";
    }
}
