package com.example.sudoku2;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class ExampleActivity extends AppCompatActivity {

    TextView textView = findViewById(R.id.myText);
    Button btn = findViewById(R.id.myBtn);

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_example);

        textView.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                textView.setText("hello");
                textView.clearComposingText();

            }
        });
    }
}
