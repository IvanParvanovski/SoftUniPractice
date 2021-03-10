package com.example.database;

import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class DataActivity extends AppCompatActivity {

    TextView textView;
    ArrayList<String> dataList;
    ListView listView;
    String nameGetStr;
    MyDataBaseHelper dbHelper;
    SQLiteDatabase database;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_data);

        textView = findViewById(R.id.name_text);
        listView = findViewById(R.id.list);
        dataList = new ArrayList<>();

        // инициираме MyDataBaseHelper в onCreate метода на MainActivity.java
        dbHelper = new MyDataBaseHelper(this);

        // отваряме БД за четене и запис
        database = dbHelper.getReadableDatabase();

        // Четене на данни от БД с метода query()
        Cursor cursor = database.query(MyDataBaseHelper.TABLE_NAME, new String[]{
                        MyDataBaseHelper.UID, MyDataBaseHelper.COLUMN_USER_NAME},
                null,
                null,
                null,
                null,
                null);
        while (cursor.moveToNext()) {

            // получаване на индексите и стойностите на колоните
            int id = cursor.getInt(cursor.getColumnIndex(MyDataBaseHelper.UID));

            nameGetStr = cursor.getString(cursor.getColumnIndex(MyDataBaseHelper.COLUMN_USER_NAME));
        }

        textView.setText(nameGetStr);

        cursor.close();

        // Втори метод за извличане на данни с метода rawQuery() и показването им в списък
        Cursor dataCursor = database.rawQuery("SELECT * FROM " + MyDataBaseHelper.TABLE_NAME, null);

        if (dataCursor.getCount() == 0) {
            Toast.makeText(DataActivity.this, "Базата от данни е празна!", Toast.LENGTH_SHORT).show();
        } else {
            while (dataCursor.moveToNext()) {
                dataList.add(dataCursor.getString(cursor.getColumnIndex(MyDataBaseHelper.COLUMN_USER_NAME)));
            }
            ArrayAdapter listAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, dataList);
            listView.setAdapter(listAdapter);
        }
        dataCursor.close();

    }

    @Override
    protected void onDestroy() {
        // затваряме връзката с БД
        database.close();
        dbHelper.close();
        super.onDestroy();
    }
}