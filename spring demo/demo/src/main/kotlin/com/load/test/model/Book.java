package com.load.test.model;

public class Book {
    private String title;
    private String IBAN;
    private Integer pages;

    public Book(String title, String IBAN, Integer pages) {
        this.title = title;
        this.IBAN = IBAN;
        this.pages = pages;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getIBAN() {
        return IBAN;
    }

    public void setIBAN(String IBAN) {
        this.IBAN = IBAN;
    }

    public Integer getPages() {
        return pages;
    }

    public void setPages(Integer pages) {
        this.pages = pages;
    }
}
