package com.example.grocerystore;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Toast;

public class Mix_Products extends AppCompatActivity {

    boolean checkBox_check = false;
    Button button_PreviousMenu, button_NextMenu;

    CheckBox checkBox_Apples, checkBox_Bananas, checkBox_Pineapples, checkBox_Strawberries;
    CheckBox checkBox_Watermelons, checkBox_Limes, checkBox_Lemons, checkBox_JavaPlums;
    CheckBox checkBox_Mangos, checkBox_Nectarines, checkBox_Oranges, checkBox_Pears;

    String string_Apples, string_Bananas, string_Pineapples, string_Strawberries = null;
    String string_Watermelons, string_Limes, string_Lemons, string_JavaPlums = null;
    String string_Mangos, string_Nectarines, string_Oranges, string_Pears = null;

    CheckBox checkBox_Carrots, checkBox_Cauliflower, checkBox_Cucumbers, checkBox_Broccoli;
    CheckBox checkBox_Potatoes, checkBox_Spinach, checkBox_Tomatoes, checkBox_Onions;
    CheckBox checkBox_Peas, checkBox_Garlic, checkBox_Mushrooms, checkBox_Pumpkin;

    String string_Carrots, string_Cauliflower, string_Cucumbers, string_Broccoli = null;
    String string_Potatoes, string_Spinach, string_Tomatoes, string_Onions = null;
    String string_Peas, string_Garlic, string_Mushrooms, string_Pumpkin = null;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mix_products);

        button_PreviousMenu = findViewById(R.id.button_PreviousMenu);
        button_NextMenu = findViewById(R.id.button_NextMenu);

        checkBox_Carrots = findViewById(R.id.checkbox_Carrots);
        checkBox_Cauliflower = findViewById(R.id.checkbox_Cauliflower);
        checkBox_Cucumbers = findViewById(R.id.checkbox_Cucumbers);
        checkBox_Broccoli = findViewById(R.id.checkbox_Broccoli);
        checkBox_Potatoes = findViewById(R.id.checkbox_Potatoes);
        checkBox_Spinach = findViewById(R.id.checkbox_Spinach);
        checkBox_Tomatoes = findViewById(R.id.checkbox_Tomatoes);
        checkBox_Onions = findViewById(R.id.checkbox_Onions);
        checkBox_Peas = findViewById(R.id.checkbox_Peas);
        checkBox_Garlic = findViewById(R.id.checkbox_Garlic);
        checkBox_Mushrooms = findViewById(R.id.checkbox_Mushrooms);
        checkBox_Pumpkin = findViewById(R.id.checkbox_Pumpkin);


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


        button_PreviousMenu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intentFruits = new Intent(Mix_Products.this, MainActivity.class);
                startActivity(intentFruits);
            }
        });


        button_NextMenu.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

                if (checkBox_Carrots.isChecked())
                {
                    string_Carrots = "string_Carrots";
                    checkBox_check = true;
                } else
                    {
                    string_Carrots = null;
                    }

                if (checkBox_Cauliflower.isChecked())
                {
                    string_Cauliflower = "string_Cauliflower";
                    checkBox_check = true;
                } else
                    {
                    string_Cauliflower = null;
                    }

                if (checkBox_Cucumbers.isChecked())
                {
                    string_Cucumbers = "string_Cucumbers";
                    checkBox_check = true;
                } else
                    {
                    string_Cucumbers = null;
                    }

                if (checkBox_Broccoli.isChecked())
                {
                    string_Broccoli = "string_Broccoli";
                    checkBox_check = true;
                } else
                    {
                    string_Broccoli = null;
                    }

                if (checkBox_Potatoes.isChecked())
                {
                    string_Potatoes = "string_Potatoes";
                    checkBox_check = true;
                } else
                    {
                    string_Potatoes = null;
                    }

                if (checkBox_Spinach.isChecked())
                {
                    string_Spinach = "string_Spinach";
                    checkBox_check = true;
                } else
                    {
                    string_Spinach = null;
                    }

                if (checkBox_Tomatoes.isChecked())
                {
                    string_Tomatoes = "string_Tomatoes";
                    checkBox_check = true;
                } else
                    {
                    string_Tomatoes = null;
                    }

                if (checkBox_Onions.isChecked())
                {
                    string_Onions = "string_Onions";
                    checkBox_check = true;
                } else
                    {
                    string_Onions = null;
                    }

                if (checkBox_Peas.isChecked())
                {
                    string_Peas = "string_Peas";
                    checkBox_check = true;
                } else
                    {
                    string_Peas = null;
                    }

                if (checkBox_Garlic.isChecked())
                {
                    string_Garlic = "string_Garlic";
                    checkBox_check = true;
                } else
                    {
                    string_Garlic = null;
                    }

                if (checkBox_Mushrooms.isChecked())
                {
                    string_Mushrooms = "string_Mushrooms";
                    checkBox_check = true;
                } else
                    {
                    string_Mushrooms = null;
                    }

                if (checkBox_Pumpkin.isChecked())
                {
                    string_Pumpkin = "string_Pumpkin";
                    checkBox_check = true;
                } else
                    {
                    string_Pumpkin = null;
                    }


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
                    Intent sendIntent = new Intent(Mix_Products.this, TotalSettings.class);

                    sendIntent.putExtra("string_Carrots", string_Carrots);
                    sendIntent.putExtra("string_Cauliflower", string_Cauliflower);
                    sendIntent.putExtra("string_Cucumbers", string_Cucumbers);
                    sendIntent.putExtra("string_Broccoli", string_Broccoli);
                    sendIntent.putExtra("string_Potatoes", string_Potatoes);
                    sendIntent.putExtra("string_Spinach", string_Spinach);
                    sendIntent.putExtra("string_Tomatoes", string_Tomatoes);
                    sendIntent.putExtra("string_Onions", string_Onions);
                    sendIntent.putExtra("string_Peas", string_Peas);
                    sendIntent.putExtra("string_Garlic", string_Garlic);
                    sendIntent.putExtra("string_Mushrooms", string_Mushrooms);
                    sendIntent.putExtra("string_Pumpkin", string_Pumpkin);
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
                    Toast.makeText(Mix_Products.this, "Моля, изберете продукт!", Toast.LENGTH_SHORT).show();
                    }


            }
        });

    }

    public void errorFix(View view){}
}
