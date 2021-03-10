package com.example.fitness;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Typeface;
import android.os.Bundle;
import android.widget.TextView;

import java.lang.reflect.Type;

public class MainActivity extends AppCompatActivity {

    TextView textView_Weight;
    Typeface poppins_Regular;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView_Weight = findViewById(R.id.textView_Weight);

        poppins_Regular = Typeface.createFromAsset(getAssets(), "Lobster-Regular.ttf");
        textView_Weight.setTypeface(poppins_Regular);
    }
}
