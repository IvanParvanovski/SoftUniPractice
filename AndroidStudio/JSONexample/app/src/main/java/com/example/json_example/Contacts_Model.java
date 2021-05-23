package com.example.json_example;

public class Contacts_Model
{
    private String mName;
    private String mEmail;
    private String mMobile;

    public Contacts_Model(String name, String email, String mobile)
    {
        this.mName = name;
        this.mEmail = email;
        this.mMobile = mobile;
    }

    public String getmName() {
        return mName;
    }

    public String getmEmail() {
        return mEmail;
    }

    public String getmMobile() {
        return mMobile;
    }
}
