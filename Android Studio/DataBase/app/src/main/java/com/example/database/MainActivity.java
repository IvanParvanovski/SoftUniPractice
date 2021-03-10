package com.example.database;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {


    EditText editText;
    Button insertButton;
    String nameSaveStr;
    MyDataBaseHelper dbHelper;
    SQLiteDatabase database;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // инициираме MyDataBaseHelper в onCreate метода на MainActivity.java
        dbHelper = new MyDataBaseHelper(this);

        // отваряме БД за четене и запис
        database = dbHelper.getWritableDatabase();

        editText = findViewById(R.id.edit_text);

        insertButton = findViewById(R.id.insert_button);
        insertButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                nameSaveStr = editText.getText().toString().trim();
                if(editText.length() != 0) {

                    // добавяне на запис
                    String insertQuery = "INSERT INTO " + MyDataBaseHelper.TABLE_NAME + " (" + MyDataBaseHelper.COLUMN_USER_NAME + ") VALUES ('" + nameSaveStr + "')";

                    database.execSQL(insertQuery);

//                ContentValues values = new ContentValues();
//                values.put(MyDataBaseHelper.COLUMN_USER_NAME, nameSaveStr);
//                database.insert(MyDataBaseHelper.TABLE_NAME, null, values);

                    Intent intent = new Intent(MainActivity.this, DataActivity.class);
                    startActivity(intent);

                } else {
                    Toast.makeText(MainActivity.this, "Моля, напишете Вашето име!", Toast.LENGTH_SHORT).show();
                }
            }
        });

    }

    @Override
    protected void onDestroy() {
        // затваряме връзката с БД
        database.close();
        dbHelper.close();
        super.onDestroy();
    }
}