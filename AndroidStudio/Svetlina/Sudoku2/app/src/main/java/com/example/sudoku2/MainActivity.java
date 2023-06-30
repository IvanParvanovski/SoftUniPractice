package com.example.sudoku2;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

//        String firstRow_leftGrid_first_test = "firstRow_leftGrid_first";
//        int resId = getResources().getIdentifier(firstRow_leftGrid_first_test, "id", getPackageName());
//        TextView textView = findViewById(resId);


public class MainActivity extends AppCompatActivity {
    TextView focused, result;
    Button check;

    ArrayList<TextView> topLeftGrid = new ArrayList<>();
    ArrayList<TextView> topMiddleGrid = new ArrayList<>();
    ArrayList<TextView> topRightGrid = new ArrayList<>();

    ArrayList<TextView> middleLeftGrid = new ArrayList<>();
    ArrayList<TextView> middleMiddleGrid = new ArrayList<>();
    ArrayList<TextView> middleRightGrid = new ArrayList<>();

    ArrayList<TextView> lastLeftGrid = new ArrayList<>();
    ArrayList<TextView> lastMiddleGrid = new ArrayList<>();
    ArrayList<TextView> lastRightGrid = new ArrayList<>();

    ArrayList<Button> controlsNumbers = new ArrayList<>();

    ArrayList<ArrayList<TextView>> grids = new ArrayList<>();

    TextView firstRow_leftGrid_first, firstRow_leftGrid_second, firstRow_leftGrid_third,
             firstRow_leftGrid_forth, firstRow_leftGrid_fifth, firstRow_leftGrid_sixth,
             firstRow_leftGrid_seventh, firstRow_leftGrid_eighth, firstRow_leftGrid_ninth;

    TextView firstRow_middleGrid_first, firstRow_middleGrid_second, firstRow_middleGrid_third,
             firstRow_middleGrid_forth, firstRow_middleGrid_fifth, firstRow_middleGrid_sixth,
             firstRow_middleGrid_seventh, firstRow_middleGrid_eighth, firstRow_middleGrid_ninth;

    TextView firstRow_rightGrid_first, firstRow_rightGrid_second, firstRow_rightGrid_third,
             firstRow_rightGrid_forth, firstRow_rightGrid_fifth, firstRow_rightGrid_sixth,
             firstRow_rightGrid_seventh, firstRow_rightGrid_eighth, firstRow_rightGrid_ninth;

    TextView middleRow_leftGrid_first, middleRow_leftGrid_second, middleRow_leftGrid_third,
             middleRow_leftGrid_forth, middleRow_leftGrid_fifth, middleRow_leftGrid_sixth,
             middleRow_leftGrid_seventh, middleRow_leftGrid_eighth, middleRow_leftGrid_ninth;

    TextView middleRow_middleGrid_first, middleRow_middleGrid_second, middleRow_middleGrid_third,
             middleRow_middleGrid_forth, middleRow_middleGrid_fifth, middleRow_middleGrid_sixth,
             middleRow_middleGrid_seventh, middleRow_middleGrid_eighth, middleRow_middleGrid_ninth;

    TextView middleRow_rightGrid_first, middleRow_rightGrid_second, middleRow_rightGrid_third,
             middleRow_rightGrid_forth, middleRow_rightGrid_fifth, middleRow_rightGrid_sixth,
             middleRow_rightGrid_seventh, middleRow_rightGrid_eighth, middleRow_rightGrid_ninth;

    TextView lastRow_leftGrid_first, lastRow_leftGrid_second, lastRow_leftGrid_third,
             lastRow_leftGrid_forth, lastRow_leftGrid_fifth, lastRow_leftGrid_sixth,
             lastRow_leftGrid_seventh, lastRow_leftGrid_eighth, lastRow_leftGrid_ninth;

    TextView lastRow_middleGrid_first, lastRow_middleGrid_second, lastRow_middleGrid_third,
             lastRow_middleGrid_forth, lastRow_middleGrid_fifth, lastRow_middleGrid_sixth,
             lastRow_middleGrid_seventh, lastRow_middleGrid_eighth, lastRow_middleGrid_ninth;

    TextView lastRow_rightGrid_first, lastRow_rightGrid_second, lastRow_rightGrid_third,
             lastRow_rightGrid_forth, lastRow_rightGrid_fifth, lastRow_rightGrid_sixth,
             lastRow_rightGrid_seventh, lastRow_rightGrid_eighth, lastRow_rightGrid_ninth;

    Button buttonOne, buttonTwo, buttonThree,
           buttonFour, buttonFive, buttonSix,
           buttonSeven, buttonEight, buttonNine;

    ArrayList<TextView> getTopLeftGrid() {
        if (topLeftGrid.size() != 0)
        {
            return topLeftGrid;
        }

        firstRow_leftGrid_first = findViewById(R.id.firstRow_leftGrid_first);
        firstRow_leftGrid_second = findViewById(R.id.firstRow_leftGrid_second);
        firstRow_leftGrid_third = findViewById(R.id.firstRow_leftGrid_third);
        firstRow_leftGrid_forth = findViewById(R.id.firstRow_leftGrid_forth);
        firstRow_leftGrid_fifth = findViewById(R.id.firstRow_leftGrid_fifth);
        firstRow_leftGrid_sixth = findViewById(R.id.firstRow_leftGrid_sixth);
        firstRow_leftGrid_seventh = findViewById(R.id.firstRow_leftGrid_seventh);
        firstRow_leftGrid_eighth = findViewById(R.id.firstRow_leftGrid_eight);
        firstRow_leftGrid_ninth = findViewById(R.id.firstRow_leftGrid_ninth);

         return new ArrayList<>(Arrays.asList(
                firstRow_leftGrid_first,
                firstRow_leftGrid_second,
                firstRow_leftGrid_third,
                firstRow_leftGrid_forth,
                firstRow_leftGrid_fifth,
                firstRow_leftGrid_sixth,
                firstRow_leftGrid_seventh,
                firstRow_leftGrid_eighth,
                firstRow_leftGrid_ninth
        ));
    }

    ArrayList<TextView> getTopMiddleGrid() {
        if (topMiddleGrid.size() != 0)
        {
            return topMiddleGrid;
        }

        firstRow_middleGrid_first = findViewById(R.id.firstRow_middleGrid_first);
        firstRow_middleGrid_second = findViewById(R.id.firstRow_middleGrid_second);
        firstRow_middleGrid_third = findViewById(R.id.firstRow_middleGrid_third);
        firstRow_middleGrid_forth = findViewById(R.id.firstRow_middleGrid_forth);
        firstRow_middleGrid_fifth = findViewById(R.id.firstRow_middleGrid_fifth);
        firstRow_middleGrid_sixth = findViewById(R.id.firstRow_middleGrid_sixth);
        firstRow_middleGrid_seventh = findViewById(R.id.firstRow_middleGrid_seventh);
        firstRow_middleGrid_eighth = findViewById(R.id.firstRow_middleGrid_eighth);
        firstRow_middleGrid_ninth = findViewById(R.id.firstRow_middleGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                firstRow_middleGrid_first,
                firstRow_middleGrid_second,
                firstRow_middleGrid_third,
                firstRow_middleGrid_forth,
                firstRow_middleGrid_fifth,
                firstRow_middleGrid_sixth,
                firstRow_middleGrid_seventh,
                firstRow_middleGrid_eighth,
                firstRow_middleGrid_ninth
        ));
    }

    ArrayList<TextView> getTopRightGrid() {
        if (topRightGrid.size() != 0)
        {
            return topRightGrid;
        }

        firstRow_rightGrid_first = findViewById(R.id.firstRow_rightGrid_first);
        firstRow_rightGrid_second = findViewById(R.id.firstRow_rightGrid_second);
        firstRow_rightGrid_third = findViewById(R.id.firstRow_rightGrid_third);
        firstRow_rightGrid_forth = findViewById(R.id.firstRow_rightGrid_forth);
        firstRow_rightGrid_fifth = findViewById(R.id.firstRow_rightGrid_fifth);
        firstRow_rightGrid_sixth = findViewById(R.id.firstRow_rightGrid_sixth);
        firstRow_rightGrid_seventh = findViewById(R.id.firstRow_rightGrid_seventh);
        firstRow_rightGrid_eighth = findViewById(R.id.firstRow_rightGrid_eighth);
        firstRow_rightGrid_ninth = findViewById(R.id.firstRow_rightGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                firstRow_rightGrid_first,
                firstRow_rightGrid_second,
                firstRow_rightGrid_third,
                firstRow_rightGrid_forth,
                firstRow_rightGrid_fifth,
                firstRow_rightGrid_sixth,
                firstRow_rightGrid_seventh,
                firstRow_rightGrid_eighth,
                firstRow_rightGrid_ninth
        ));
    }

    ArrayList<TextView> getMiddleLeftGrid() {
        if (middleLeftGrid.size() != 0)
        {
            return middleLeftGrid;
        }

        middleRow_leftGrid_first = findViewById(R.id.middleRow_leftGrid_first);
        middleRow_leftGrid_second = findViewById(R.id.middleRow_leftGrid_second);
        middleRow_leftGrid_third = findViewById(R.id.middleRow_leftGrid_third);
        middleRow_leftGrid_forth = findViewById(R.id.middleRow_leftGrid_forth);
        middleRow_leftGrid_fifth = findViewById(R.id.middleRow_leftGrid_fifth);
        middleRow_leftGrid_sixth = findViewById(R.id.middleRow_leftGrid_sixth);
        middleRow_leftGrid_seventh = findViewById(R.id.middleRow_leftGrid_seventh);
        middleRow_leftGrid_eighth = findViewById(R.id.middleRow_leftGrid_eighth);
        middleRow_leftGrid_ninth = findViewById(R.id.middleRow_leftGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                middleRow_leftGrid_first,
                middleRow_leftGrid_second,
                middleRow_leftGrid_third,
                middleRow_leftGrid_forth,
                middleRow_leftGrid_fifth,
                middleRow_leftGrid_sixth,
                middleRow_leftGrid_seventh,
                middleRow_leftGrid_eighth,
                middleRow_leftGrid_ninth
        ));
    }

    ArrayList<TextView> getMiddleMiddleGrid() {
        if (middleMiddleGrid.size() != 0)
        {
            return middleMiddleGrid;
        }

        middleRow_middleGrid_first = findViewById(R.id.middleRow_middleGrid_first);
        middleRow_middleGrid_second = findViewById(R.id.middleRow_middleGrid_second);
        middleRow_middleGrid_third = findViewById(R.id.middleRow_middleGrid_third);
        middleRow_middleGrid_forth = findViewById(R.id.middleRow_middleGrid_forth);
        middleRow_middleGrid_fifth = findViewById(R.id.middleRow_middleGrid_fifth);
        middleRow_middleGrid_sixth = findViewById(R.id.middleRow_middleGrid_sixth);
        middleRow_middleGrid_seventh = findViewById(R.id.middleRow_middleGrid_seventh);
        middleRow_middleGrid_eighth = findViewById(R.id.middleRow_middleGrid_eighth);
        middleRow_middleGrid_ninth = findViewById(R.id.middleRow_middleGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                middleRow_middleGrid_first,
                middleRow_middleGrid_second,
                middleRow_middleGrid_third,
                middleRow_middleGrid_forth,
                middleRow_middleGrid_fifth,
                middleRow_middleGrid_sixth,
                middleRow_middleGrid_seventh,
                middleRow_middleGrid_eighth,
                middleRow_middleGrid_ninth
        ));
    }

    ArrayList<TextView> getMiddleRightGrid() {
        if (middleRightGrid.size() != 0)
        {
            return middleRightGrid;
        }

        middleRow_rightGrid_first = findViewById(R.id.middleRow_rightGrid_first);
        middleRow_rightGrid_second = findViewById(R.id.middleRow_rightGrid_second);
        middleRow_rightGrid_third = findViewById(R.id.middleRow_rightGrid_third);
        middleRow_rightGrid_forth = findViewById(R.id.middleRow_rightGrid_forth);
        middleRow_rightGrid_fifth = findViewById(R.id.middleRow_rightGrid_fifth);
        middleRow_rightGrid_sixth = findViewById(R.id.middleRow_rightGrid_sixth);
        middleRow_rightGrid_seventh = findViewById(R.id.middleRow_rightGrid_seventh);
        middleRow_rightGrid_eighth = findViewById(R.id.middleRow_rightGrid_eighth);
        middleRow_rightGrid_ninth = findViewById(R.id.middleRow_rightGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                middleRow_rightGrid_first,
                middleRow_rightGrid_second,
                middleRow_rightGrid_third,
                middleRow_rightGrid_forth,
                middleRow_rightGrid_fifth,
                middleRow_rightGrid_sixth,
                middleRow_rightGrid_seventh,
                middleRow_rightGrid_eighth,
                middleRow_rightGrid_ninth
        ));
    }

    ArrayList<TextView> getLastLeftGrid() {
        if (lastLeftGrid.size() != 0)
        {
            return lastLeftGrid;
        }

        lastRow_leftGrid_first = findViewById(R.id.lastRow_leftGrid_first);
        lastRow_leftGrid_second = findViewById(R.id.lastRow_leftGrid_second);
        lastRow_leftGrid_third = findViewById(R.id.lastRow_leftGrid_third);
        lastRow_leftGrid_forth = findViewById(R.id.lastRow_leftGrid_forth);
        lastRow_leftGrid_fifth = findViewById(R.id.lastRow_leftGrid_fifth);
        lastRow_leftGrid_sixth = findViewById(R.id.lastRow_leftGrid_sixth);
        lastRow_leftGrid_seventh = findViewById(R.id.lastRow_leftGrid_seventh);
        lastRow_leftGrid_eighth = findViewById(R.id.lastRow_leftGrid_eighth);
        lastRow_leftGrid_ninth = findViewById(R.id.lastRow_leftGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                lastRow_leftGrid_first,
                lastRow_leftGrid_second,
                lastRow_leftGrid_third,
                lastRow_leftGrid_forth,
                lastRow_leftGrid_fifth,
                lastRow_leftGrid_sixth,
                lastRow_leftGrid_seventh,
                lastRow_leftGrid_eighth,
                lastRow_leftGrid_ninth
        ));
    }

    ArrayList<TextView> getLastMiddleGrid() {
        if (lastMiddleGrid.size() != 0)
        {
            return lastMiddleGrid;
        }

        lastRow_middleGrid_first = findViewById(R.id.lastRow_middleGrid_first);
        lastRow_middleGrid_second = findViewById(R.id.lastRow_middleGrid_second);
        lastRow_middleGrid_third = findViewById(R.id.lastRow_middleGrid_third);
        lastRow_middleGrid_forth = findViewById(R.id.lastRow_middleGrid_forth);
        lastRow_middleGrid_fifth = findViewById(R.id.lastRow_middleGrid_fifth);
        lastRow_middleGrid_sixth = findViewById(R.id.lastRow_middleGrid_sixth);
        lastRow_middleGrid_seventh = findViewById(R.id.lastRow_middleGrid_seventh);
        lastRow_middleGrid_eighth = findViewById(R.id.lastRow_middleGrid_eighth);
        lastRow_middleGrid_ninth = findViewById(R.id.lastRow_middleGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                lastRow_middleGrid_first,
                lastRow_middleGrid_second,
                lastRow_middleGrid_third,
                lastRow_middleGrid_forth,
                lastRow_middleGrid_fifth,
                lastRow_middleGrid_sixth,
                lastRow_middleGrid_seventh,
                lastRow_middleGrid_eighth,
                lastRow_middleGrid_ninth
        ));
    }

    ArrayList<TextView> getLastRightGrid() {
        if (lastRightGrid.size() != 0)
        {
            return lastRightGrid;
        }

        lastRow_rightGrid_first = findViewById(R.id.lastRow_rightGrid_first);
        lastRow_rightGrid_second = findViewById(R.id.lastRow_rightGrid_second);
        lastRow_rightGrid_third = findViewById(R.id.lastRow_rightGrid_third);
        lastRow_rightGrid_forth = findViewById(R.id.lastRow_rightGrid_forth);
        lastRow_rightGrid_fifth = findViewById(R.id.lastRow_rightGrid_fifth);
        lastRow_rightGrid_sixth = findViewById(R.id.lastRow_rightGrid_sixth);
        lastRow_rightGrid_seventh = findViewById(R.id.lastRow_rightGrid_seventh);
        lastRow_rightGrid_eighth = findViewById(R.id.lastRow_rightGrid_eighth);
        lastRow_rightGrid_ninth = findViewById(R.id.lastRow_rightGrid_ninth);

        return new ArrayList<>(Arrays.asList(
                lastRow_rightGrid_first,
                lastRow_rightGrid_second,
                lastRow_rightGrid_third,
                lastRow_rightGrid_forth,
                lastRow_rightGrid_fifth,
                lastRow_rightGrid_sixth,
                lastRow_rightGrid_seventh,
                lastRow_rightGrid_eighth,
                lastRow_rightGrid_ninth
        ));
    }

    ArrayList<Button> getControlsNumbers() {
        if (controlsNumbers.size() != 0)
        {
            return controlsNumbers;
        }

        buttonOne = findViewById(R.id.button_one);
        buttonTwo = findViewById(R.id.button_two);
        buttonThree = findViewById(R.id.button_three);
        buttonFour = findViewById(R.id.button_four);
        buttonFive = findViewById(R.id.button_five);
        buttonSix = findViewById(R.id.button_six);
        buttonSeven = findViewById(R.id.button_seven);
        buttonEight = findViewById(R.id.button_eighth);
        buttonNine = findViewById(R.id.button_nine);

        return new ArrayList<>(Arrays.asList(
            buttonOne,
            buttonTwo,
            buttonThree,
            buttonFour,
            buttonFive,
            buttonSix,
            buttonSeven,
            buttonEight,
            buttonNine
        ));
    }

    ArrayList<ArrayList<TextView>> getRows() {
        ArrayList<TextView> first_row = new ArrayList<>(Arrays.asList(
                firstRow_leftGrid_first, firstRow_leftGrid_second, firstRow_leftGrid_third,
                firstRow_middleGrid_first, firstRow_middleGrid_second, firstRow_middleGrid_third,
                firstRow_rightGrid_first, firstRow_rightGrid_second, firstRow_rightGrid_third
        ));

        ArrayList<TextView> second_row = new ArrayList<>(Arrays.asList(
                firstRow_leftGrid_forth, firstRow_leftGrid_fifth, firstRow_leftGrid_sixth,
                firstRow_middleGrid_forth, firstRow_middleGrid_fifth, firstRow_middleGrid_sixth,
                firstRow_rightGrid_forth, firstRow_rightGrid_fifth, firstRow_rightGrid_sixth
        ));

        ArrayList<TextView> third_row = new ArrayList<>(Arrays.asList(
                firstRow_leftGrid_seventh, firstRow_leftGrid_eighth, firstRow_leftGrid_ninth,
                firstRow_middleGrid_seventh, firstRow_middleGrid_eighth, firstRow_middleGrid_ninth,
                firstRow_rightGrid_seventh, firstRow_rightGrid_eighth, firstRow_rightGrid_ninth
        ));

        ArrayList<TextView> forth_row = new ArrayList<>(Arrays.asList(
                middleRow_leftGrid_first, middleRow_leftGrid_second, middleRow_leftGrid_third,
                middleRow_middleGrid_first, middleRow_middleGrid_second, middleRow_middleGrid_third,
                middleRow_rightGrid_first, middleRow_rightGrid_second, middleRow_rightGrid_third
        ));

        ArrayList<TextView> fifth_row = new ArrayList<>(Arrays.asList(
                middleRow_leftGrid_forth, middleRow_leftGrid_fifth, middleRow_leftGrid_sixth,
                middleRow_middleGrid_forth, middleRow_middleGrid_fifth, middleRow_middleGrid_sixth,
                middleRow_rightGrid_forth, middleRow_rightGrid_fifth, middleRow_rightGrid_sixth
        ));

        ArrayList<TextView> sixth_row = new ArrayList<>(Arrays.asList(
                middleRow_leftGrid_seventh, middleRow_leftGrid_eighth, middleRow_leftGrid_ninth,
                middleRow_middleGrid_seventh, middleRow_middleGrid_eighth, middleRow_middleGrid_ninth,
                middleRow_rightGrid_seventh, middleRow_rightGrid_eighth, middleRow_rightGrid_ninth
        ));

        ArrayList<TextView> seventh_row = new ArrayList<>(Arrays.asList(
                lastRow_leftGrid_first, lastRow_leftGrid_second, lastRow_leftGrid_third,
                lastRow_middleGrid_first, lastRow_middleGrid_second, lastRow_middleGrid_third,
                lastRow_rightGrid_first, lastRow_rightGrid_second, lastRow_rightGrid_third
        ));

        ArrayList<TextView> eighth_row = new ArrayList<>(Arrays.asList(
                lastRow_leftGrid_forth, lastRow_leftGrid_fifth, lastRow_leftGrid_sixth,
                lastRow_middleGrid_forth, lastRow_middleGrid_fifth, lastRow_middleGrid_sixth,
                lastRow_rightGrid_forth, lastRow_rightGrid_fifth, lastRow_rightGrid_sixth
        ));

        ArrayList<TextView> ninth_row = new ArrayList<>(Arrays.asList(
                lastRow_leftGrid_seventh, lastRow_leftGrid_eighth, lastRow_leftGrid_ninth,
                lastRow_middleGrid_seventh, lastRow_middleGrid_eighth, lastRow_middleGrid_ninth,
                lastRow_rightGrid_seventh, lastRow_rightGrid_eighth, lastRow_rightGrid_ninth
        ));

        return new ArrayList<>(Arrays.asList(
                first_row, second_row, third_row,
                forth_row, fifth_row, sixth_row,
                seventh_row, eighth_row, ninth_row
        ));
    }

    ArrayList<ArrayList<TextView>> getColumns() {
        ArrayList<TextView> first_col = new ArrayList<>(Arrays.asList(
                firstRow_leftGrid_first, firstRow_leftGrid_forth, firstRow_leftGrid_seventh,
                middleRow_leftGrid_first, middleRow_leftGrid_forth, middleRow_leftGrid_seventh,
                lastRow_leftGrid_first, lastRow_leftGrid_forth, lastRow_leftGrid_seventh
        ));

        ArrayList<TextView> second_col = new ArrayList<>(Arrays.asList(
                firstRow_leftGrid_second, firstRow_leftGrid_fifth, firstRow_leftGrid_eighth,
                middleRow_leftGrid_second, middleRow_leftGrid_fifth, middleRow_leftGrid_eighth,
                lastRow_leftGrid_second, lastRow_leftGrid_fifth, lastRow_leftGrid_eighth
        ));

        ArrayList<TextView> third_col = new ArrayList<>(Arrays.asList(
                firstRow_leftGrid_third, firstRow_leftGrid_sixth, firstRow_leftGrid_ninth,
                middleRow_leftGrid_third, middleRow_leftGrid_sixth, middleRow_leftGrid_ninth,
                lastRow_leftGrid_third, lastRow_leftGrid_sixth, lastRow_leftGrid_ninth
        ));

        ArrayList<TextView> forth_col = new ArrayList<>(Arrays.asList(
                firstRow_middleGrid_first, firstRow_middleGrid_forth, firstRow_middleGrid_seventh,
                middleRow_middleGrid_first, middleRow_middleGrid_forth, middleRow_middleGrid_seventh,
                lastRow_middleGrid_first, lastRow_middleGrid_forth, lastRow_middleGrid_seventh
        ));

        ArrayList<TextView> fifth_col = new ArrayList<>(Arrays.asList(
                firstRow_middleGrid_second, firstRow_middleGrid_fifth, firstRow_middleGrid_eighth,
                middleRow_middleGrid_second, middleRow_middleGrid_fifth, middleRow_middleGrid_eighth,
                lastRow_middleGrid_second, lastRow_middleGrid_fifth, lastRow_middleGrid_eighth
        ));

        ArrayList<TextView> sixth_col = new ArrayList<>(Arrays.asList(
                firstRow_middleGrid_third, firstRow_middleGrid_sixth, firstRow_middleGrid_ninth,
                middleRow_middleGrid_third, middleRow_middleGrid_sixth, middleRow_middleGrid_ninth,
                lastRow_middleGrid_third, lastRow_middleGrid_sixth, lastRow_middleGrid_ninth
        ));

        ArrayList<TextView> seventh_col = new ArrayList<>(Arrays.asList(
                firstRow_rightGrid_first, firstRow_rightGrid_forth, firstRow_rightGrid_seventh,
                middleRow_rightGrid_first, middleRow_rightGrid_forth, middleRow_rightGrid_seventh,
                lastRow_rightGrid_first, lastRow_rightGrid_forth, lastRow_rightGrid_seventh
        ));

        ArrayList<TextView> eighth_col = new ArrayList<>(Arrays.asList(
                firstRow_rightGrid_second, firstRow_rightGrid_fifth, firstRow_rightGrid_eighth,
                middleRow_rightGrid_second, middleRow_rightGrid_fifth, middleRow_rightGrid_eighth,
                lastRow_rightGrid_second, lastRow_rightGrid_fifth, lastRow_rightGrid_eighth
        ));

        ArrayList<TextView> ninth_col = new ArrayList<>(Arrays.asList(
                firstRow_rightGrid_third, firstRow_rightGrid_sixth, firstRow_rightGrid_ninth,
                middleRow_rightGrid_third, middleRow_rightGrid_sixth, middleRow_rightGrid_ninth,
                lastRow_rightGrid_third, lastRow_rightGrid_sixth, lastRow_rightGrid_ninth
        ));

        return new ArrayList<>(Arrays.asList(
                first_col, second_col, third_col,
                forth_col, fifth_col, sixth_col,
                seventh_col, eighth_col, ninth_col
        ));
    }

    ArrayList<TextView> setNumbers = new ArrayList<>();

    @SuppressLint("SetTextI18n")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        int[][] generatedSudokuGrid = generateSudoku();

        // Get Grids

        topLeftGrid = getTopLeftGrid();
        topMiddleGrid = getTopMiddleGrid();
        topRightGrid = getTopRightGrid();

        middleLeftGrid = getMiddleLeftGrid();
        middleMiddleGrid = getMiddleMiddleGrid();
        middleRightGrid = getMiddleRightGrid();

        lastLeftGrid = getLastLeftGrid();
        lastMiddleGrid = getLastMiddleGrid();
        lastRightGrid = getLastRightGrid();

        grids.add(topLeftGrid);
        grids.add(topMiddleGrid);
        grids.add(topRightGrid);

        grids.add(middleLeftGrid);
        grids.add(middleMiddleGrid);
        grids.add(middleRightGrid);

        grids.add(lastLeftGrid);
        grids.add(lastMiddleGrid);
        grids.add(lastRightGrid);


        // Controls and result of game

        result = findViewById(R.id.resultTextView);
        check = findViewById(R.id.checkBtn);
        focused = firstRow_leftGrid_first;

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                Random toSet = new Random();

                if (toSet.nextBoolean()){
                    TextView temp = getRows().get(row).get(col);

                    System.out.println(row + " - " + col + ", " + temp );
                    temp.setText(Integer.toString(generatedSudokuGrid[row][col]));
                    setNumbers.add(temp);
                }
            }
        }
        setFocusedStyle();

        // Set Numbers (Buttons) to change box content

        ArrayList<Button> controlsNumbers = getControlsNumbers();

        setClickEventsOnNumbersBtn(controlsNumbers);
        setClickEventsOnTextViews(grids);

        // Check Game Status

        check.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View view) {
                Boolean gridsStatus = getCollectionsStatus(grids);
                Boolean rowsStatus = getCollectionsStatus(getRows());
                Boolean colsStatus = getCollectionsStatus(getColumns());

                System.out.println("Grids: " + gridsStatus);
                System.out.println("Rows: " + rowsStatus);
                System.out.println("Cols: " + colsStatus);

                if (gridsStatus && rowsStatus && colsStatus) {
                    result.setText("Correct!");
                    result.setTextColor(Color.GREEN);
                }
                else {
                    result.setText("Wrong!");
                    result.setTextColor(Color.RED);

                }
            }
        });

        System.out.println("success");
    }

    void setFocusedStyle() {
        focused.setTextColor(Color.rgb(44, 115, 210));
        focused.setTextSize(TypedValue.COMPLEX_UNIT_SP, 32);
    }

    void resetFocusedStyle() {
        focused.setTextColor(Color.GRAY);
        focused.setTextSize(TypedValue.COMPLEX_UNIT_SP, 24);
    }

    public int[][] generateSudoku() {
        Random random = new Random();
        int[][] grid = new int[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                grid[i][j] = 0;
            }
        }

        for (int i = 0; i < 9; i++) {
            System.out.println("Row Started " + i );

            int j = 0;



            for (; j < 9; j++) {
                int num = random.nextInt(9) + 1;

                System.out.print(num + " in, ");
                Map<Integer, Boolean> visitedNumbers = new HashMap<>() {{
                    put(1, false);
                    put(2, false);
                    put(3, false);
                    put(4, false);
                    put(5, false);
                    put(6, false);
                    put(7, false);
                    put(8, false);
                    put(9, false);
                }};

                int count = 0;
                while (isValid(grid, i, j, num)) {
                    num = random.nextInt(9) + 1;
                    System.out.println("here " + count);

                    boolean allTrue = true;

                    for (Boolean value: visitedNumbers.values())
                    {
                        if (!value)
                        {
                            allTrue = false;
                            break;
                        }
                    }

                    // All visited numbers should be true to reset
                    if (allTrue){
                        System.out.println("Reset Row");
                        Arrays.fill(grid[i], 0);
                        j = 0;
                    }

                    visitedNumbers.put(num, true);
                    count++;
                }

                System.out.println(num + " out");
                grid[i][j] = num;
            }

            System.out.println(Arrays.toString(grid[i]));
        }

        System.out.println("end");

        for (int i = 0; i < 9; i++) {
            for (int l = 0; l < 9; l++){
                System.out.print(grid[i][l] + " ");
            }
            System.out.println();
        }

        return grid;
    }

    private boolean isValid(int[][] grid, int row, int col, int num) {
        // check if the number is already in the row
        for (int i = 0; i < 9; i++) {
            if (grid[row][i] == num) {
                return true;
            }
        }

        // check if the number is already in the column
        for (int i = 0; i < 9; i++) {
            if (grid[i][col] == num) {
                return true;
            }
        }

        // check if the number is already in the 3x3 subgrid
        int subgridRow = row / 3 * 3;
        int subgridCol = col / 3 * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[subgridRow + i][subgridCol + j] == num) {
                    return true;
                }
            }
        }

        return false;
    }


    Boolean getCollectionsStatus(ArrayList<ArrayList<TextView>> collections) {
        for (ArrayList<TextView> elements : collections) {
            Boolean status = checkCollectionStatus(elements);
            if (!status) {
                return false;
            }
        }

        return true;

    }

    Boolean checkCollectionStatus(ArrayList<TextView> elements) {
        Map<String, Boolean> existingNumbers = new HashMap<>() {{
            put("1", false);
            put("2", false);
            put("3", false);
            put("4", false);
            put("5", false);
            put("6", false);
            put("7", false);
            put("8", false);
            put("9", false);
        }};

        for (int i = 0; i < elements.size(); i++) {
            String temp = (String) elements.get(i).getText();

            if (!existingNumbers.containsKey(temp)) {
                return false;
            }

            existingNumbers.put(temp, true);
        }

        for (Boolean status : existingNumbers.values()) {
            if (!status) {
                return false;
            }
        }

        return true;
    }

    void setClickEventsOnTextViews(ArrayList<ArrayList<TextView>> elements) {
        for (ArrayList<TextView> collection : elements) {
            for (TextView el: collection) {

                el.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        resetFocusedStyle();
                        TextView temp = (TextView) view;

                        if (!setNumbers.contains(temp)) {
                            focused = (TextView) view;
                        }

                        setFocusedStyle();
                    }
                });
            }
        }
    }

    void setClickEventsOnNumbersBtn(ArrayList<Button> controls) {
        for (Button controlBtn : controls) {
            controlBtn.setOnClickListener(v -> {
                Button btn = (Button) v;
                focused.setText(btn.getText().toString());
            });
        }
    }
}
