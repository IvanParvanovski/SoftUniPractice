package com.example.mydatabasehelper;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    String nameSaveStr;
    Button button_Submit;
    EditText editText;
    SQLiteDatabase database;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editText = findViewById(R.id.editText_id);
        button_Submit = findViewById(R.id.buttonSubmit_id);
        //inicializirame database
        MyDataBaseHelper dbHelper = new MyDataBaseHelper(this);
        database = dbHelper.getWritableDatabase();

       button_Submit.setOnClickListener(new View.OnClickListener() {
           @Override
           public void onClick(View v) {
               nameSaveStr = editText.getText().toString().trim();

               if (editText.length() != 0){
                   //we set information or content which our user gave us
                   String insterQuery = "INSERT INTO " + MyDataBaseHelper.TABLE_NAME + " (" + MyDataBaseHelper.COLUMN_USER_NAME + ") VALUES (" + nameSaveStr + ")";
                   //izpulvame komandata insterQuery
                   database.execSQL(insterQuery);

                   Intent intent = new Intent(MainActivity.this, DataActivity.class);
                   startActivity(intent);
               }else{
                   Toast.makeText(MainActivity.this, "Please type your name!", Toast.LENGTH_SHORT).show();
               }
           }
       });

//        ContentValues values = new ContentValues();
//        values.put(MyDataBaseHelper.COLUMN_USER_NAME, "uname");
//        database.insert(MyDataBaseHelper.TABLE_NAME,null,values);


        //we close the database after the things we have added
        database.close();
        dbHelper.close();

    }
}
