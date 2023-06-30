package com.example.changeactivities;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class AdditionalDataActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_additional_data);

        Button btn = findViewById(R.id.btnSubmit);

        EditText etPhone = findViewById(R.id.etPhone);
        EditText etAddress = findViewById(R.id.etAdd);

        Intent intent = getIntent();

        String firstName = intent.getStringExtra("FirstName");
        String lastName = intent.getStringExtra("LastName");
        String age = intent.getStringExtra("Age");

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent dataInt = new Intent(getApplicationContext(), ShowDataActivity.class);

                dataInt.putExtra("Phone", etPhone.getText().toString());
                dataInt.putExtra("Address", etAddress.getText().toString());

                dataInt.putExtra("FirstName", firstName);
                dataInt.putExtra("LastName", lastName);
                dataInt.putExtra("Age", age);

                startActivity(dataInt);
            }
        });


    }
}