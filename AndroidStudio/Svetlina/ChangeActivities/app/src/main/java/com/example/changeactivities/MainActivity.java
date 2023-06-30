package com.example.changeactivities;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.widget.Toolbar;

import java.util.ArrayList;
import java.util.List;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText etFirstName = findViewById(R.id.etFirstName);
        EditText etLastName = findViewById(R.id.etLastName);
        EditText etAge = findViewById(R.id.etAge);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        List<Item> items = new ArrayList<Item>();
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));
        items.add(new Item("John Wick", "john.wick@email.com", R.drawable.a1));
        items.add(new Item("Emo Romo", "john.wick@email.com", R.drawable.a3));

//        RecyclerView recyclerView = findViewById(R.id.recyclerView);
//        recyclerView.setLayoutManager(new LinearLayoutManager(this));
//        recyclerView.setAdapter(new MyAdapter(getApplicationContext(), items));

        Button btn = findViewById(R.id.btnNext);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String firstName = etFirstName.getText().toString();
                String lastName = etLastName.getText().toString();
                String age = etAge.getText().toString();

                Intent dataInt = new Intent(getApplicationContext(), AdditionalDataActivity.class);

                dataInt.putExtra("FirstName", firstName);
                dataInt.putExtra("LastName", lastName);
                dataInt.putExtra("Age", age);

                startActivity(dataInt);
            }
        });
    }
}