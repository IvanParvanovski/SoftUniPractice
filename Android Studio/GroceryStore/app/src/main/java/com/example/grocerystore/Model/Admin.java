package com.example.grocerystore.Model;

import com.example.grocerystore.AdminDataActivity;

import java.util.ArrayList;

public class Admin {
    int id;
    String username, password, address, populated_place, first_name, last_name, age;

    public Admin(int id, String username, String password, String address, String populated_place, String first_name, String last_name, String age) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.address = address;
        this.populated_place = populated_place;
        this.first_name = first_name;
        this.last_name = last_name;
        this.age = age;
    }
    public Admin(AdminDataActivity adminDataActivity, ArrayList<Admin> adminArrayList){}

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPopulated_place() {
        return populated_place;
    }

    public void setPopulated_place(String populated_place) {
        this.populated_place = populated_place;
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
}
