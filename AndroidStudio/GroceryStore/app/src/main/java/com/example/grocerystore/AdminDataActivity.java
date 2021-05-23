package com.example.grocerystore;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.grocerystore.Adapters.AdminAdapter;
import com.example.grocerystore.Model.Admin;

import java.util.ArrayList;

public class AdminDataActivity extends AppCompatActivity
{

    TextView textView;
    ArrayList<String> dataList;
    ArrayList<Admin> adminArrayList;
    AdminAdapter adminAdapter;
    ListView listView;
    String nameGetStr;
    AdminDataBaseHelper dbHelper;
    SQLiteDatabase database;
    AdminDataBaseHelper adminDataBaseHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_admin_data);

        listView = findViewById(R.id.listView);
        dataList = new ArrayList<>();
        adminDataBaseHelper = new AdminDataBaseHelper(this);
        adminArrayList = new ArrayList<>();
        loadDataInListView();


   }

   private void loadDataInListView()
   {
        adminArrayList = adminDataBaseHelper.getAllData();
        adminAdapter = new AdminAdapter(this, adminArrayList);
        listView.setAdapter(adminAdapter);
        adminAdapter.notifyDataSetChanged();
   }



}




