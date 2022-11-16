package com.example.sudoku2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // First Row
    TextView firstRow_leftGrid_first = findViewById(R.id.firstRow_leftGrid_first);
    TextView firstRow_leftGrid_second = findViewById(R.id.firstRow_leftGrid_second);
    TextView firstRow_leftGrid_third = findViewById(R.id.firstRow_leftGrid_third);
    TextView firstRow_leftGrid_forth = findViewById(R.id.firstRow_leftGrid_forth);
    TextView firstRow_leftGrid_fifth = findViewById(R.id.firstRow_leftGrid_fifth);
    TextView firstRow_leftGrid_sixth = findViewById(R.id.firstRow_leftGrid_sixth);
    TextView firstRow_leftGrid_seventh = findViewById(R.id.firstRow_leftGrid_seventh);
    TextView firstRow_leftGrid_eighth = findViewById(R.id.firstRow_leftGrid_eight);
    TextView firstRow_leftGrid_ninth = findViewById(R.id.firstRow_leftGrid_ninth);

    TextView firstRow_middleGrid_first = findViewById(R.id.firstRow_middleGrid_first);
    TextView firstRow_middleGrid_second = findViewById(R.id.firstRow_middleGrid_second);
    TextView firstRow_middleGrid_third = findViewById(R.id.firstRow_middleGrid_third);
    TextView firstRow_middleGrid_forth = findViewById(R.id.firstRow_middleGrid_forth);
    TextView firstRow_middleGrid_fifth = findViewById(R.id.firstRow_middleGrid_fifth);
    TextView firstRow_middleGrid_sixth = findViewById(R.id.firstRow_middleGrid_sixth);
    TextView firstRow_middleGrid_seventh = findViewById(R.id.firstRow_middleGrid_seventh);
    TextView firstRow_middleGrid_eighth = findViewById(R.id.firstRow_middleGrid_eighth);
    TextView firstRow_middleGrid_ninth = findViewById(R.id.firstRow_middleGrid_ninth);

    TextView firstRow_rightGrid_first = findViewById(R.id.firstRow_rightGrid_first);
    TextView firstRow_rightGrid_second = findViewById(R.id.firstRow_rightGrid_second);
    TextView firstRow_rightGrid_third = findViewById(R.id.firstRow_rightGrid_third);
    TextView firstRow_rightGrid_forth = findViewById(R.id.firstRow_rightGrid_forth);
    TextView firstRow_rightGrid_fifth = findViewById(R.id.firstRow_rightGrid_fifth);
    TextView firstRow_rightGrid_sixth = findViewById(R.id.firstRow_rightGrid_sixth);
    TextView firstRow_rightGrid_seventh = findViewById(R.id.firstRow_rightGrid_seventh);
    TextView firstRow_rightGrid_eighth = findViewById(R.id.firstRow_rightGrid_eighth);
    TextView firstRow_rightGrid_ninth = findViewById(R.id.firstRow_rightGrid_ninth);

    // Second Row

    TextView middleRow_leftGrid_first = findViewById(R.id.middleRow_leftGrid_first);
    TextView middleRow_leftGrid_second = findViewById(R.id.middleRow_leftGrid_second);
    TextView middleRow_leftGrid_third = findViewById(R.id.middleRow_leftGrid_third);
    TextView middleRow_leftGrid_forth = findViewById(R.id.middleRow_leftGrid_forth);
    TextView middleRow_leftGrid_fifth = findViewById(R.id.middleRow_leftGrid_fifth);
    TextView middleRow_leftGrid_sixth = findViewById(R.id.middleRow_leftGrid_sixth);
    TextView middleRow_leftGrid_seventh = findViewById(R.id.middleRow_leftGrid_seventh);
    TextView middleRow_leftGrid_eighth = findViewById(R.id.middleRow_leftGrid_eighth);
    TextView middleRow_leftGrid_ninth = findViewById(R.id.middleRow_leftGrid_ninth);

    TextView middleRow_middleGrid_first = findViewById(R.id.middleRow_middleGrid_first);
    TextView middleRow_middleGrid_second = findViewById(R.id.middleRow_middleGrid_second);
    TextView middleRow_middleGrid_third = findViewById(R.id.middleRow_middleGrid_third);
    TextView middleRow_middleGrid_forth = findViewById(R.id.middleRow_middleGrid_forth);
    TextView middleRow_middleGrid_fifth = findViewById(R.id.middleRow_middleGrid_fifth);
    TextView middleRow_middleGrid_sixth = findViewById(R.id.middleRow_middleGrid_sixth);
    TextView middleRow_middleGrid_seventh = findViewById(R.id.middleRow_middleGrid_seventh);
    TextView middleRow_middleGrid_eighth = findViewById(R.id.middleRow_middleGrid_eighth);
    TextView middleRow_middleGrid_ninth = findViewById(R.id.middleRow_middleGrid_ninth);

    TextView middleRow_rightGrid_first = findViewById(R.id.middleRow_rightGrid_first);
    TextView middleRow_rightGrid_second = findViewById(R.id.middleRow_rightGrid_second);
    TextView middleRow_rightGrid_third = findViewById(R.id.middleRow_rightGrid_third);
    TextView middleRow_rightGrid_forth = findViewById(R.id.middleRow_rightGrid_forth);
    TextView middleRow_rightGrid_fifth = findViewById(R.id.middleRow_rightGrid_fifth);
    TextView middleRow_rightGrid_sixth = findViewById(R.id.middleRow_rightGrid_sixth);
    TextView middleRow_rightGrid_seventh = findViewById(R.id.middleRow_rightGrid_seventh);
    TextView middleRow_rightGrid_eighth = findViewById(R.id.middleRow_rightGrid_eighth);
    TextView middleRow_rightGrid_ninth = findViewById(R.id.middleRow_rightGrid_ninth);

    // Third Row

    TextView lastRow_leftGrid_first = findViewById(R.id.lastRow_leftGrid_first);
    TextView lastRow_leftGrid_second = findViewById(R.id.lastRow_leftGrid_second);
    TextView lastRow_leftGrid_third = findViewById(R.id.lastRow_leftGrid_third);
    TextView lastRow_leftGrid_forth = findViewById(R.id.lastRow_leftGrid_forth);
    TextView lastRow_leftGrid_fifth = findViewById(R.id.lastRow_leftGrid_fifth);
    TextView lastRow_leftGrid_sixth = findViewById(R.id.lastRow_leftGrid_sixth);
    TextView lastRow_leftGrid_seventh = findViewById(R.id.lastRow_leftGrid_seventh);
    TextView lastRow_leftGrid_eighth = findViewById(R.id.lastRow_leftGrid_eighth);
    TextView lastRow_leftGrid_ninth = findViewById(R.id.lastRow_leftGrid_ninth);

    TextView lastRow_middleGrid_first = findViewById(R.id.lastRow_middleGrid_first);
    TextView lastRow_middleGrid_second = findViewById(R.id.lastRow_middleGrid_second);
    TextView lastRow_middleGrid_third = findViewById(R.id.lastRow_middleGrid_third);
    TextView lastRow_middleGrid_forth = findViewById(R.id.lastRow_middleGrid_forth);
    TextView lastRow_middleGrid_fifth = findViewById(R.id.lastRow_middleGrid_fifth);
    TextView lastRow_middleGrid_sixth = findViewById(R.id.lastRow_middleGrid_sixth);
    TextView lastRow_middleGrid_seventh = findViewById(R.id.lastRow_middleGrid_seventh);
    TextView lastRow_middleGrid_eighth = findViewById(R.id.lastRow_middleGrid_eighth);
    TextView lastRow_middleGrid_ninth = findViewById(R.id.lastRow_middleGrid_ninth);

    TextView lastRow_rightGrid_first = findViewById(R.id.lastRow_rightGrid_first);
    TextView lastRow_rightGrid_second = findViewById(R.id.lastRow_rightGrid_second);
    TextView lastRow_rightGrid_third = findViewById(R.id.lastRow_rightGrid_third);
    TextView lastRow_rightGrid_forth = findViewById(R.id.lastRow_rightGrid_forth);
    TextView lastRow_rightGrid_fifth = findViewById(R.id.lastRow_rightGrid_fifth);
    TextView lastRow_rightGrid_sixth = findViewById(R.id.lastRow_rightGrid_sixth);
    TextView lastRow_rightGrid_seventh = findViewById(R.id.lastRow_rightGrid_seventh);
    TextView lastRow_rightGrid_eighth = findViewById(R.id.lastRow_rightGrid_eighth);
    TextView lastRow_rightGrid_ninth = findViewById(R.id.lastRow_rightGrid_ninth);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}