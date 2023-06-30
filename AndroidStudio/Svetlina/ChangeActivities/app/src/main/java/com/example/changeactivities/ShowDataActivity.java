package com.example.changeactivities;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.w3c.dom.Text;

public class ShowDataActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_data);

        Button btn = findViewById(R.id.btnHome);

        Intent intent = getIntent();

        String firstName = intent.getStringExtra("FirstName");
        String lastName = intent.getStringExtra("LastName");
        String age = intent.getStringExtra("Age");

        String phone = intent.getStringExtra("Phone");
        String address = intent.getStringExtra("Address");

        TextView tvFirstName = findViewById(R.id.tvFirstName);
        TextView tvLastName = findViewById(R.id.tvLastName);
        TextView tvAge = findViewById(R.id.tvAge);
        TextView tvPhone = findViewById(R.id.tvPhone);
        TextView tvAddress = findViewById(R.id.tvAddress);

        tvFirstName.setText(firstName);
        tvLastName.setText(lastName);
        tvAge.setText(age);
        tvPhone.setText(phone);
        tvAddress.setText(address);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent homeInt = new Intent(getApplicationContext(), MainActivity.class);

                startActivity(homeInt);
            }
        });
    }
}