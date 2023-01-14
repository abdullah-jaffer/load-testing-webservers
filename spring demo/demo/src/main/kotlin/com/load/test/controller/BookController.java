package com.load.test.controller;

import com.load.test.model.Book;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("book")
public class BookController {
    @GetMapping("/")
    public Book getBook() {
        return new Book("Domain Driven Design", "AL35202111090000000001234567", 426);
    }
}