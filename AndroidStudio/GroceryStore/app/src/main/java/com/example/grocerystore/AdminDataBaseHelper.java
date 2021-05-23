package com.example.grocerystore;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import androidx.annotation.Nullable;

import com.example.grocerystore.Model.Admin;

import java.util.ArrayList;

public class AdminDataBaseHelper extends SQLiteOpenHelper
{
    private static final String DATABASE_NAME = "User_DataBase.db";
    private static final int DATABASE_VERSION = 11;

    public AdminDataBaseHelper(@Nullable Context context)
    {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    public final static String TABLE_NAME = "User_Information";

    public final static String Column_1 = "ID";
    public final static String Column_2 = "Username";
    public final static String Column_3 = "Password";
    public final static String Column_4 = "Address";
    public final static String Column_5 = "Populated_Place";
    public final static String Column_6 = "First_Name";
    public final static String Column_7 = "Last_Name";
    public final static String Column_8 = "Age";

    @Override
    public void onCreate(SQLiteDatabase database)
    {
        String create_ItemTable = "CREATE TABLE " + TABLE_NAME + " (" + Column_1 + " INTEGER PRIMARY KEY AUTOINCREMENT, " + Column_2 + " TEXT NOT NULL, " + Column_3 + " TEXT NOT NULL, " + Column_4 + " TEXT NOT NULL, " + Column_5 + " TEXT NOT NULL, " + Column_6 + " TEXT NOT NULL, " + Column_7 + " TEXT NOT NULL, " + Column_8 + " TEXT NOT NULL);";
        database.execSQL(create_ItemTable);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion)
    {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);
        onCreate(db);
    }

    public ArrayList<Admin> getAllData()
    {
        ArrayList<Admin> arrayList = new ArrayList<>();
        SQLiteDatabase db = this.getReadableDatabase();
        Cursor cursor = db.rawQuery("SELECT * FROM " + TABLE_NAME, null);

        while (cursor.moveToNext())
        {
            int Id = cursor.getInt(0);
            String Username = cursor.getString(1);
            String Password = cursor.getString(2);
            String Address = cursor.getString(3);
            String PopulatedPlace = cursor.getString(4);
            String FirstName = cursor.getString(5);
            String LastName = cursor.getString(6);
            String Age = cursor.getString(7);

            Admin admin = new Admin(Id, Username, Password, Address, PopulatedPlace, FirstName, LastName, Age);
            arrayList.add(admin);
        }
        return arrayList;
    }
}
