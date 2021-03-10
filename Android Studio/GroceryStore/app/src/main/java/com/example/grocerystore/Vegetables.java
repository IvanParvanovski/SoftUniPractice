package com.example.grocerystore;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Toast;

public class Vegetables extends AppCompatActivity {

    CheckBox checkBox_Carrots, checkBox_Cauliflower, checkBox_Cucumbers, checkBox_Broccoli;
    CheckBox checkBox_Potatoes, checkBox_Spinach, checkBox_Tomatoes, checkBox_Onions;
    CheckBox checkBox_Peas, checkBox_Garlic, checkBox_Mushrooms, checkBox_Pumpkin;

    boolean checkBox_check = false;

    String string_Carrots, string_Cauliflower, string_Cucumbers, string_Broccoli = null;
    String string_Potatoes, string_Spinach, string_Tomatoes, string_Onions = null;
    String string_Peas, string_Garlic, string_Mushrooms, string_Pumpkin = null;

    Button button_PreviousMenu, button_NextMenu;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_vegetables);


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


        button_PreviousMenu.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intentFruits = new Intent(Vegetables.this, MainActivity.class);
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

                if (checkBox_check)
                {
                    Intent sendIntent = new Intent(Vegetables.this, Vegetables_TotalSettings.class);

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
                    startActivity(sendIntent);
                } else
                    {
                    Toast.makeText(Vegetables.this, "Моля, изберете продукт!", Toast.LENGTH_SHORT).show();
                    }
            }
        });

    }

    public void errorFix(View view) {}
}
