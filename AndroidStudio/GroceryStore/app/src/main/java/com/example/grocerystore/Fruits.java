package com.example.grocerystore;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Toast;

public class Fruits extends AppCompatActivity
{


    Button button_PreviousMenu, button_NextMenu;
    double total_sum = 0;

    CheckBox checkBox_Apples, checkBox_Bananas, checkBox_Pineapples, checkBox_Strawberries;
    CheckBox checkBox_Watermelons, checkBox_Limes, checkBox_Lemons, checkBox_JavaPlums;
    CheckBox checkBox_Mangos, checkBox_Nectarines, checkBox_Oranges, checkBox_Pears;

    boolean checkBox_check = false;

    String string_Apples, string_Bananas, string_Pineapples, string_Strawberries = null;
    String string_Watermelons, string_Limes, string_Lemons, string_JavaPlums = null;
    String string_Mangos, string_Nectarines, string_Oranges, string_Pears = null;


    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fruits);


        button_PreviousMenu = findViewById(R.id.button_PreviousMenu);
        button_NextMenu = findViewById(R.id.button_NextMenu);

        checkBox_Apples = findViewById(R.id.checkbox_Apples);
        checkBox_Bananas = findViewById(R.id.checkbox_Bananas);
        checkBox_Pineapples = findViewById(R.id.checkbox_Pineapples);
        checkBox_Strawberries = findViewById(R.id.checkbox_Strawberries);
        checkBox_Watermelons = findViewById(R.id.checkbox_Watermelons);
        checkBox_Limes = findViewById(R.id.checkbox_Limes);
        checkBox_Lemons = findViewById(R.id.checkbox_Lemons);
        checkBox_JavaPlums = findViewById(R.id.checkbox_JavaPlums);
        checkBox_Mangos = findViewById(R.id.checkbox_Mangos);
        checkBox_Nectarines = findViewById(R.id.checkbox_Nectarines);
        checkBox_Oranges = findViewById(R.id.checkbox_Oranges);
        checkBox_Pears = findViewById(R.id.checkbox_Pears);


        button_NextMenu.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

                //Check the checkBoxes

                if (checkBox_Apples.isChecked())
                {
                    string_Apples = "string_Apples";
                    checkBox_check = true;
                } else
                    {
                    string_Apples = null;
                    }

                if (checkBox_Bananas.isChecked())
                {
                    string_Bananas = "string_Bananas";
                    checkBox_check = true;
                } else
                    {
                    string_Bananas = null;
                    }

                if (checkBox_Pineapples.isChecked())
                {
                    string_Pineapples = "string_Pineapples";
                    checkBox_check = true;
                } else
                    {
                    string_Pineapples = null;
                    }

                if (checkBox_Strawberries.isChecked())
                {
                    string_Strawberries = "string_Strawberries";
                    checkBox_check = true;
                } else
                    {
                    string_Strawberries = null;
                    }

                if (checkBox_Watermelons.isChecked())
                {
                    string_Watermelons = "string_Watermelons";
                    checkBox_check = true;
                } else
                    {
                    string_Watermelons = null;
                    }

                if (checkBox_Limes.isChecked())
                {
                    string_Limes = "string_Limes";
                    checkBox_check = true;
                } else
                    {
                    string_Limes = null;
                    }

                if (checkBox_Lemons.isChecked())
                {
                    string_Lemons = "string_Lemons";
                    checkBox_check = true;
                } else
                    {
                    string_Lemons = null;
                    }

                if (checkBox_JavaPlums.isChecked())
                {
                    string_JavaPlums = "string_JavaPlums";
                    checkBox_check = true;
                } else
                    {
                    string_JavaPlums = null;
                    }

                if (checkBox_Mangos.isChecked())
                {
                    string_Mangos = "string_Mangos";
                    checkBox_check = true;
                } else
                    {
                    string_Mangos = null;
                    }

                if (checkBox_Nectarines.isChecked())
                {
                    string_Nectarines = "string_Nectarines";
                    checkBox_check = true;
                } else
                    {
                    string_Nectarines = null;
                    }

                if (checkBox_Oranges.isChecked())
                {
                    string_Oranges = "string_Oranges";
                    checkBox_check = true;
                } else
                    {
                    string_Oranges = null;
                    }

                if (checkBox_Pears.isChecked())
                {
                    string_Pears = "string_Pears";
                    checkBox_check = true;
                } else
                    {
                    string_Pears = null;
                    }

                if (checkBox_check)
                {
                    Intent sendIntent = new Intent(Fruits.this, Fruits_TotalSettings.class);

                    sendIntent.putExtra("string_Apples", string_Apples);
                    sendIntent.putExtra("string_Bananas", string_Bananas);
                    sendIntent.putExtra("string_Pineapples", string_Pineapples);
                    sendIntent.putExtra("string_Strawberries", string_Strawberries);
                    sendIntent.putExtra("string_Watermelons", string_Watermelons);
                    sendIntent.putExtra("string_Limes", string_Limes);
                    sendIntent.putExtra("string_Lemons", string_Lemons);
                    sendIntent.putExtra("string_JavaPlums", string_JavaPlums);
                    sendIntent.putExtra("string_Mangos", string_Mangos);
                    sendIntent.putExtra("string_Nectarines", string_Nectarines);
                    sendIntent.putExtra("string_Oranges", string_Oranges);
                    sendIntent.putExtra("string_Pears", string_Pears);
                    startActivity(sendIntent);
                } else
                    {
                    Toast.makeText(Fruits.this, "Моля, изберете продукт!", Toast.LENGTH_SHORT).show();
                    }
            }
        });

        button_PreviousMenu.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intentFruits = new Intent(Fruits.this, MainActivity.class);
                startActivity(intentFruits);
            }
        });

    }

    public void errorFix(View view){}


}


