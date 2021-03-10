
package com.example.grocerystore;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.text.DecimalFormat;
import java.text.NumberFormat;

import static java.lang.String.valueOf;


public class TotalSettings extends AppCompatActivity {

    LinearLayout linearLayout_Carrots, linearLayout_Cauliflower, linearLayout_Cucumbers, linearLayout_Broccoli;
    LinearLayout linearLayout_Potatoes, linearLayout_Spinach, linearLayout_Tomatoes, linearLayout_Onion;
    LinearLayout linearLayout_Pumpkins, linearLayout_Peas, linearLayout_Garlic, linearLayout_Mushrooms;
    LinearLayout linearLayout_Apples, linearLayout_Bananas, linearLayout_Pineapples, linearLayout_Strawberries;
    LinearLayout linearLayout_Watermelons, linearLayout_Limes, linearLayout_Lemons, linearLayout_JavaPlums;
    LinearLayout linearLayout_Mangos, linearLayout_Nectarines, linearLayout_Oranges, linearLayout_Pears;

    TextView textView_Carrots, textView_Cauliflower, textView_Cucumbers, textView_Broccoli;
    TextView textView_Potatoes, textView_Spinach, textView_Tomatoes, textView_Onion;
    TextView textView_Pumpkins, textView_Peas, textView_Garlic, textView_Mushrooms;
    TextView textView_Apples, textView_Bananas, textView_Pineapples, textView_Strawberries;
    TextView textView_Watermelons, textView_Limes, textView_Lemons, textView_JavaPlums;
    TextView textView_Mangos, textView_Nectarines, textView_Oranges, textView_Pears;

    String string_Carrots, string_Cauliflower, string_Cucumbers, string_Broccoli;
    String string_Potatoes, string_Spinach, string_Tomatoes, string_Onions;
    String string_Pumpkin, string_Peas, string_Garlic, string_Mushrooms;
    String string_Apples, string_Bananas, string_Pineapples, string_Strawberries;
    String string_Watermelons, string_Limes, string_Lemons, string_JavaPlums;
    String string_Mangos, string_Nectarines, string_Oranges, string_Pears;

    Button button_Plus_Carrots, button_Plus_Cauliflower, button_Plus_Cucumbers, button_Plus_Broccoli;
    Button button_Plus_Potatoes, button_Plus_Spinach, button_Plus_Tomatoes, button_Plus_Onion;
    Button button_Plus_Pumpkins, button_Plus_Peas, button_Plus_Garlic, button_Plus_Mushrooms;
    Button button_Plus_Apples, button_Plus_Bananas, button_Plus_Pineapples, button_Plus_Strawberries;
    Button button_Plus_Watermelons, button_Plus_Limes, button_Plus_Lemons, button_Plus_JavaPlums;
    Button button_Plus_Mangos, button_Plus_Nectarines, button_Plus_Oranges, button_Plus_Pears;

    Button button_Minus_Carrots, button_Minus_Cauliflower, button_Minus_Cucumbers, button_Minus_Broccoli;
    Button button_Minus_Potatoes, button_Minus_Spinach, button_Minus_Tomatoes, button_Minus_Onion;
    Button button_Minus_Pumpkins, button_Minus_Peas, button_Minus_Garlic, button_Minus_Mushrooms;
    Button button_Minus_Apples, button_Minus_Bananas, button_Minus_Pineapples, button_Minus_Strawberries;
    Button button_Minus_Watermelons, button_Minus_Limes, button_Minus_Lemons, button_Minus_JavaPlums;
    Button button_Minus_Mangos, button_Minus_Nectarines, button_Minus_Oranges, button_Minus_Pears;

    TextView textView_Counter_Carrots, textView_Counter_Cauliflower, textView_Counter_Cucumbers, textView_Counter_Broccoli;
    TextView textView_Counter_Potatoes, textView_Counter_Spinach, textView_Counter_Tomatoes, textView_Counter_Onion;
    TextView textView_Counter_Pumpkins, textView_Counter_Peas, textView_Counter_Garlic, textView_Counter_Mushrooms;
    TextView textView_Counter_Apples, textView_Counter_Bananas, textView_Counter_Pineapples, textView_Counter_Strawberries;
    TextView textView_Counter_Watermelons, textView_Counter_Limes, textView_Counter_Lemons, textView_Counter_JavaPlums;
    TextView textView_Counter_Mangos, textView_Counter_Nectarines, textView_Counter_Oranges, textView_Counter_Pears;

    String toast_MaxCounter = "Не можете да поръчате повече от 100kg!";
    String toast_MinCounter = "Не можете да поръчате по-малко от 1kg!";

    int carrots_Counter = 1;
    int cauliflower_Counter = 1;
    int cucumbers_Counter = 1;
    int broccoli_Counter = 1;
    int potatoes_Counter = 1;
    int spinach_Counter = 1;
    int tomatoes_Counter = 1;
    int onion_Counter = 1;
    int pumpkins_Counter = 1;
    int peas_Counter = 1;
    int garlic_Counter = 1;
    int mushrooms_Counter = 1;

    int apples_Counter = 1;
    int bananas_Counter = 1;
    int pineapples_Counter = 1;
    int strawberries_Counter = 1;
    int watermelons_Counter = 1;
    int limes_Counter = 1;
    int lemons_Counter = 1;
    int javaPlums_Counter = 1;
    int mangos_Counter = 1;
    int nectarines_Counter = 1;
    int oranges_Counter = 1;
    int pears_Counter = 1;
    boolean checkSubmitButton = false;
    String emailText;

    double carrots_price = 0.97;
    double cauliflower_price = 1.54;
    double cucumbers_price = 1.43;
    double broccoli_price = 2.18;
    double potatoes_price = 1.67;
    double spinach_price = 1.20;
    double tomatoes_price = 2.18;
    double onion_price = 0.76;
    double pumpkins_price = 1.13;
    double peas_price = 2.18;
    double garlic_price = 0.76;
    double mushrooms_price = 2.16;

    double apples_price = 1.67;
    double bananas_price = 1.40;
    double pineapples_price = 1.67;
    double strawberries_price = 2.47;
    double watermelons_price = 1.12;
    double limes_price = 1.24;
    double lemons_price = 0.56;
    double javaPlums_price = 1.23;
    double mangos_price = 1.23;
    double nectarines_price = 1.43;
    double oranges_price = 0.67;
    double pears_price = 1.87;

    Button button_Submit;
    Button button_Order;
    Button button_PreviousMenu;
    double total_sum = 0;
    TextView textView_TotalNumber;

    double carrots_sum, cauliflower_sum, cucumbers_sum, broccoli_sum;
    double potatoes_sum, spinach_sum, tomatoes_sum, onion_sum;
    double pumpkins_sum, peas_sum, garlic_sum, mushrooms_sum;
    double apples_sum, bananas_sum, pineapple_sum, strawberries_sum;
    double watermelons_sum, limes_sum, lemons_sum, javaplums_sum;
    double mangos_sum, nectarines_sum, oranges_sum, pears_sum;

    DecimalFormat sumFormat = new DecimalFormat("#.##");
    int checkLowAm = 1;
    String kg = "kg.";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_total_settings);

        //V E G E T A B L E S

        linearLayout_Carrots = findViewById(R.id.linearLayout_Carrots);
        linearLayout_Cauliflower = findViewById(R.id.linearLayout_Cauliflower);
        linearLayout_Cucumbers = findViewById(R.id.linearLayout_Cucumbers);
        linearLayout_Broccoli = findViewById(R.id.linearLayout_Broccoli);
        linearLayout_Potatoes = findViewById(R.id.linearLayout_Potatoes);
        linearLayout_Spinach = findViewById(R.id.linearLayout_Spinach);
        linearLayout_Tomatoes = findViewById(R.id.linearLayout_Tomatoes);
        linearLayout_Onion = findViewById(R.id.linearLayout_Onion);
        linearLayout_Pumpkins = findViewById(R.id.linearLayout_Pumpkins);
        linearLayout_Peas = findViewById(R.id.linearLayout_Peas);
        linearLayout_Garlic = findViewById(R.id.linearLayout_Garlic);
        linearLayout_Mushrooms = findViewById(R.id.linearLayout_Mushrooms);

        textView_Carrots = findViewById(R.id.textView_Carrots);
        textView_Cauliflower = findViewById(R.id.textView_Cauliflower);
        textView_Cucumbers = findViewById(R.id.textView_Cucumbers);
        textView_Broccoli = findViewById(R.id.textView_Broccoli);
        textView_Potatoes = findViewById(R.id.textView_Potatoes);
        textView_Spinach = findViewById(R.id.textView_Spinach);
        textView_Tomatoes = findViewById(R.id.textView_Tomatoes);
        textView_Onion = findViewById(R.id.textView_Onion);
        textView_Pumpkins = findViewById(R.id.textView_Pumpkins);
        textView_Peas = findViewById(R.id.textView_Peas);
        textView_Garlic = findViewById(R.id.textView_Garlic);
        textView_Mushrooms = findViewById(R.id.textView_Mushrooms);

        button_Plus_Carrots = findViewById(R.id.button_Plus_Carrots);
        button_Plus_Cauliflower = findViewById(R.id.button_Plus_Cauliflower);
        button_Plus_Cucumbers = findViewById(R.id.button_Plus_Cucumbers);
        button_Plus_Broccoli = findViewById(R.id.button_Plus_Broccoli);
        button_Plus_Potatoes = findViewById(R.id.button_Plus_Potatoes);
        button_Plus_Spinach = findViewById(R.id.button_Plus_Spinach);
        button_Plus_Tomatoes = findViewById(R.id.button_Plus_Tomatoes);
        button_Plus_Onion = findViewById(R.id.button_Plus_Onion);
        button_Plus_Pumpkins = findViewById(R.id.button_Plus_Pumpkins);
        button_Plus_Peas = findViewById(R.id.button_Plus_Peas);
        button_Plus_Garlic = findViewById(R.id.button_Plus_Garlic);
        button_Plus_Mushrooms = findViewById(R.id.button_Plus_Mushrooms);

        button_Minus_Carrots = findViewById(R.id.button_Minus_Carrots);
        button_Minus_Cauliflower = findViewById(R.id.button_Minus_Cauliflower);
        button_Minus_Cucumbers = findViewById(R.id.button_Minus_Cucumbers);
        button_Minus_Broccoli = findViewById(R.id.button_Minus_Broccoli);
        button_Minus_Potatoes = findViewById(R.id.button_Minus_Potatoes);
        button_Minus_Spinach = findViewById(R.id.button_Minus_Spinach);
        button_Minus_Tomatoes = findViewById(R.id.button_Minus_Tomatoes);
        button_Minus_Onion = findViewById(R.id.button_Minus_Onion);
        button_Minus_Pumpkins = findViewById(R.id.button_Minus_Pumpkins);
        button_Minus_Peas = findViewById(R.id.button_Minus_Peas);
        button_Minus_Garlic = findViewById(R.id.button_Minus_Garlic);
        button_Minus_Mushrooms = findViewById(R.id.button_Minus_Mushrooms);

        textView_Counter_Carrots = findViewById(R.id.textView_Counter_Carrots);
        textView_Counter_Cauliflower = findViewById(R.id.textView_Counter_Cauliflower);
        textView_Counter_Cucumbers = findViewById(R.id.textView_Counter_Cucumbers);
        textView_Counter_Broccoli = findViewById(R.id.textView_Counter_Broccoli);
        textView_Counter_Potatoes = findViewById(R.id.textView_Counter_Potatoes);
        textView_Counter_Spinach = findViewById(R.id.textView_Counter_Spinach);
        textView_Counter_Tomatoes = findViewById(R.id.textView_Counter_Tomatoes);
        textView_Counter_Onion = findViewById(R.id.textView_Counter_Onion);
        textView_Counter_Pumpkins = findViewById(R.id.textView_Counter_Pumpkins);
        textView_Counter_Peas = findViewById(R.id.textView_Counter_Peas);
        textView_Counter_Garlic = findViewById(R.id.textView_Counter_Garlic);
        textView_Counter_Mushrooms = findViewById(R.id.textView_Counter_Mushrooms);

        linearLayout_Carrots.setVisibility(View.GONE);
        linearLayout_Cauliflower.setVisibility(View.GONE);
        linearLayout_Cucumbers.setVisibility(View.GONE);
        linearLayout_Broccoli.setVisibility(View.GONE);
        linearLayout_Potatoes.setVisibility(View.GONE);
        linearLayout_Spinach.setVisibility(View.GONE);
        linearLayout_Tomatoes.setVisibility(View.GONE);
        linearLayout_Onion.setVisibility(View.GONE);
        linearLayout_Pumpkins.setVisibility(View.GONE);
        linearLayout_Peas.setVisibility(View.GONE);
        linearLayout_Garlic.setVisibility(View.GONE);
        linearLayout_Mushrooms.setVisibility(View.GONE);

        textView_Carrots.setVisibility(View.GONE);
        textView_Cauliflower.setVisibility(View.GONE);
        textView_Cucumbers.setVisibility(View.GONE);
        textView_Broccoli.setVisibility(View.GONE);
        textView_Potatoes.setVisibility(View.GONE);
        textView_Spinach.setVisibility(View.GONE);
        textView_Tomatoes.setVisibility(View.GONE);
        textView_Onion.setVisibility(View.GONE);
        textView_Pumpkins.setVisibility(View.GONE);
        textView_Peas.setVisibility(View.GONE);
        textView_Garlic.setVisibility(View.GONE);
        textView_Mushrooms.setVisibility(View.GONE);

        //F R U I T S

        linearLayout_Apples = findViewById(R.id.linearLayout_Apples);
        linearLayout_Bananas = findViewById(R.id.linearLayout_Bananas);
        linearLayout_Pineapples = findViewById(R.id.linearLayout_Pineapples);
        linearLayout_Strawberries = findViewById(R.id.linearLayout_Strawberries);
        linearLayout_Watermelons = findViewById(R.id.linearLayout_Watermelons);
        linearLayout_Limes = findViewById(R.id.linearLayout_Limes);
        linearLayout_Lemons = findViewById(R.id.linearLayout_Lemons);
        linearLayout_JavaPlums = findViewById(R.id.linearLayout_JavaPlums);
        linearLayout_Mangos = findViewById(R.id.linearLayout_Mangos);
        linearLayout_Nectarines = findViewById(R.id.linearLayout_Nectarines);
        linearLayout_Oranges = findViewById(R.id.linearLayout_Oranges);
        linearLayout_Pears = findViewById(R.id.linearLayout_Pears);

        textView_Apples = findViewById(R.id.textView_Apples);
        textView_Bananas = findViewById(R.id.textView_Bananas);
        textView_Pineapples = findViewById(R.id.textView_Pineapples);
        textView_Strawberries = findViewById(R.id.textView_Strawberries);
        textView_Watermelons = findViewById(R.id.textView_Watermelons);
        textView_Limes = findViewById(R.id.textView_Limes);
        textView_Lemons = findViewById(R.id.textView_Lemons);
        textView_JavaPlums = findViewById(R.id.textView_JavaPlums);
        textView_Mangos = findViewById(R.id.textView_Mangos);
        textView_Nectarines = findViewById(R.id.textView_Nectarines);
        textView_Oranges = findViewById(R.id.textView_Oranges);
        textView_Pears = findViewById(R.id.textView_Pears);

        button_Plus_Apples = findViewById(R.id.button_Plus_Apples);
        button_Plus_Bananas = findViewById(R.id.button_Plus_Bananas);
        button_Plus_Pineapples = findViewById(R.id.button_Plus_Pineapples);
        button_Plus_Strawberries = findViewById(R.id.button_Plus_Strawberries);
        button_Plus_Watermelons = findViewById(R.id.button_Plus_Watermelons);
        button_Plus_Limes = findViewById(R.id.button_Plus_Limes);
        button_Plus_Lemons = findViewById(R.id.button_Plus_Lemons);
        button_Plus_JavaPlums = findViewById(R.id.button_Plus_JavaPlums);
        button_Plus_Mangos = findViewById(R.id.button_Plus_Mangos);
        button_Plus_Nectarines = findViewById(R.id.button_Plus_Nectarines);
        button_Plus_Oranges = findViewById(R.id.button_Plus_Oranges);
        button_Plus_Pears = findViewById(R.id.button_Plus_Pears);

        button_Minus_Apples = findViewById(R.id.button_Minus_Apples);
        button_Minus_Bananas = findViewById(R.id.button_Minus_Bananas);
        button_Minus_Pineapples = findViewById(R.id.button_Minus_Pineapples);
        button_Minus_Strawberries = findViewById(R.id.button_Minus_Strawberries);
        button_Minus_Watermelons = findViewById(R.id.button_Minus_Watermelons);
        button_Minus_Limes = findViewById(R.id.button_Minus_Limes);
        button_Minus_Lemons = findViewById(R.id.button_Minus_Lemons);
        button_Minus_JavaPlums = findViewById(R.id.button_Minus_JavaPlums);
        button_Minus_Mangos = findViewById(R.id.button_Minus_Mangos);
        button_Minus_Nectarines = findViewById(R.id.button_Minus_Nectarines);
        button_Minus_Oranges = findViewById(R.id.button_Minus_Oranges);
        button_Minus_Pears = findViewById(R.id.button_Minus_Pears);

        textView_Counter_Apples = findViewById(R.id.textView_Counter_Apples);
        textView_Counter_Bananas = findViewById(R.id.textView_Counter_Bananas);
        textView_Counter_Pineapples = findViewById(R.id.textView_Counter_Pineapples);
        textView_Counter_Strawberries = findViewById(R.id.textView_Counter_Strawberries);
        textView_Counter_Watermelons = findViewById(R.id.textView_Counter_Watermelons);
        textView_Counter_Limes = findViewById(R.id.textView_Counter_Limes);
        textView_Counter_Lemons = findViewById(R.id.textView_Counter_Lemons);
        textView_Counter_JavaPlums = findViewById(R.id.textView_Counter_JavaPlums);
        textView_Counter_Mangos = findViewById(R.id.textView_Counter_Mangos);
        textView_Counter_Nectarines = findViewById(R.id.textView_Counter_Nectarines);
        textView_Counter_Oranges = findViewById(R.id.textView_Counter_Oranges);
        textView_Counter_Pears = findViewById(R.id.textView_Counter_Pears);

        linearLayout_Apples.setVisibility(View.GONE);
        linearLayout_Bananas.setVisibility(View.GONE);
        linearLayout_Pineapples.setVisibility(View.GONE);
        linearLayout_Strawberries.setVisibility(View.GONE);
        linearLayout_Watermelons.setVisibility(View.GONE);
        linearLayout_Limes.setVisibility(View.GONE);
        linearLayout_Lemons.setVisibility(View.GONE);
        linearLayout_JavaPlums.setVisibility(View.GONE);
        linearLayout_Mangos.setVisibility(View.GONE);
        linearLayout_Nectarines.setVisibility(View.GONE);
        linearLayout_Oranges.setVisibility(View.GONE);
        linearLayout_Pears.setVisibility(View.GONE);

        textView_Apples.setVisibility(View.GONE);
        textView_Bananas.setVisibility(View.GONE);
        textView_Pineapples.setVisibility(View.GONE);
        textView_Strawberries.setVisibility(View.GONE);
        textView_Watermelons.setVisibility(View.GONE);
        textView_Limes.setVisibility(View.GONE);
        textView_Lemons.setVisibility(View.GONE);
        textView_JavaPlums.setVisibility(View.GONE);
        textView_Mangos.setVisibility(View.GONE);
        textView_Nectarines.setVisibility(View.GONE);
        textView_Oranges.setVisibility(View.GONE);
        textView_Pears.setVisibility(View.GONE);

        //O T H E R S

        button_Submit = findViewById(R.id.button_Submit);
        button_Order = findViewById(R.id.button_Order);
        button_PreviousMenu = findViewById(R.id.button_PreviousMenu);
        textView_TotalNumber = findViewById(R.id.textView_TotalNumber);

        //Checking if checkbox is checked and changing the visibility of our TextViews and Layouts.

        Bundle extras = getIntent().getExtras();
        if (extras != null)
        {

            string_Carrots = extras.getString("string_Carrots");
            if (string_Carrots != null && !string_Carrots.isEmpty())
            {
                textView_Carrots.setVisibility(View.VISIBLE);
                linearLayout_Carrots.setVisibility(View.VISIBLE);
            }

            string_Cauliflower = extras.getString("string_Cauliflower");
            if (string_Cauliflower != null && !string_Cauliflower.isEmpty())
            {
                textView_Cauliflower.setVisibility(View.VISIBLE);
                linearLayout_Cauliflower.setVisibility(View.VISIBLE);
            }

            string_Cucumbers = extras.getString("string_Cucumbers");
            if (string_Cucumbers != null && !string_Cucumbers.isEmpty())
            {
                textView_Cucumbers.setVisibility(View.VISIBLE);
                linearLayout_Cucumbers.setVisibility(View.VISIBLE);
            }

            string_Broccoli = extras.getString("string_Broccoli");
            if (string_Broccoli != null && !string_Broccoli.isEmpty())
            {
                textView_Broccoli.setVisibility(View.VISIBLE);
                linearLayout_Broccoli.setVisibility(View.VISIBLE);
            }

            string_Potatoes = extras.getString("string_Potatoes");
            if (string_Potatoes != null && !string_Potatoes.isEmpty())
            {
                textView_Potatoes.setVisibility(View.VISIBLE);
                linearLayout_Potatoes.setVisibility(View.VISIBLE);
            }

            string_Spinach = extras.getString("string_Spinach");
            if (string_Spinach != null && !string_Spinach.isEmpty())
            {
                textView_Spinach.setVisibility(View.VISIBLE);
                linearLayout_Spinach.setVisibility(View.VISIBLE);
            }

            string_Tomatoes = extras.getString("string_Tomatoes");
            if (string_Tomatoes != null && !string_Tomatoes.isEmpty())
            {
                textView_Tomatoes.setVisibility(View.VISIBLE);
                linearLayout_Tomatoes.setVisibility(View.VISIBLE);
            }

            string_Onions = extras.getString("string_Onions");
            if (string_Onions != null && !string_Onions.isEmpty())
            {
                textView_Onion.setVisibility(View.VISIBLE);
                linearLayout_Onion.setVisibility(View.VISIBLE);
            }

            string_Pumpkin = extras.getString("string_Pumpkin");
            if (string_Pumpkin != null && !string_Pumpkin.isEmpty())
            {
                textView_Pumpkins.setVisibility(View.VISIBLE);
                linearLayout_Pumpkins.setVisibility(View.VISIBLE);
            }

            string_Peas = extras.getString("string_Peas");
            if (string_Peas != null && !string_Peas.isEmpty())
            {
                textView_Peas.setVisibility(View.VISIBLE);
                linearLayout_Peas.setVisibility(View.VISIBLE);
            }

            string_Garlic = extras.getString("string_Garlic");
            if (string_Garlic != null && !string_Garlic.isEmpty())
            {
                textView_Garlic.setVisibility(View.VISIBLE);
                linearLayout_Garlic.setVisibility(View.VISIBLE);
            }

            string_Mushrooms = extras.getString("string_Mushrooms");
            if (string_Mushrooms != null && !string_Mushrooms.isEmpty())
            {
                textView_Mushrooms.setVisibility(View.VISIBLE);
                linearLayout_Mushrooms.setVisibility(View.VISIBLE);
            }

            string_Apples = extras.getString("string_Apples");
            if (string_Apples != null && !string_Apples.isEmpty())
            {
                textView_Apples.setVisibility(View.VISIBLE);
                linearLayout_Apples.setVisibility(View.VISIBLE);
            }

            string_Bananas = extras.getString("string_Bananas");
            if (string_Bananas != null && !string_Bananas.isEmpty())
            {
                textView_Bananas.setVisibility(View.VISIBLE);
                linearLayout_Bananas.setVisibility(View.VISIBLE);
            }

            string_Pineapples = extras.getString("string_Pineapples");
            if (string_Pineapples != null && !string_Pineapples.isEmpty())
            {
                textView_Pineapples.setVisibility(View.VISIBLE);
                linearLayout_Pineapples.setVisibility(View.VISIBLE);
            }

            string_Strawberries = extras.getString("string_Strawberries");
            if (string_Strawberries != null && !string_Strawberries.isEmpty())
            {
                textView_Strawberries.setVisibility(View.VISIBLE);
                linearLayout_Strawberries.setVisibility(View.VISIBLE);
            }

            string_Watermelons = extras.getString("string_Watermelons");
            if (string_Watermelons != null && !string_Watermelons.isEmpty())
            {
                textView_Watermelons.setVisibility(View.VISIBLE);
                linearLayout_Watermelons.setVisibility(View.VISIBLE);
            }

            string_Limes = extras.getString("string_Limes");
            if (string_Limes != null && !string_Limes.isEmpty())
            {
                textView_Limes.setVisibility(View.VISIBLE);
                linearLayout_Limes.setVisibility(View.VISIBLE);
            }

            string_Lemons = extras.getString("string_Lemons");
            if (string_Lemons != null && !string_Lemons.isEmpty())
            {
                textView_Lemons.setVisibility(View.VISIBLE);
                linearLayout_Lemons.setVisibility(View.VISIBLE);
            }
            string_JavaPlums = extras.getString("string_JavaPlums");
            if (string_JavaPlums != null && !string_JavaPlums.isEmpty())
            {
                textView_JavaPlums.setVisibility(View.VISIBLE);
                linearLayout_JavaPlums.setVisibility(View.VISIBLE);
            }

            string_Mangos = extras.getString("string_Mangos");
            if (string_Mangos != null && !string_Mangos.isEmpty())
            {
                textView_Mangos.setVisibility(View.VISIBLE);
                linearLayout_Mangos.setVisibility(View.VISIBLE);
            }

            string_Nectarines = extras.getString("string_Nectarines");
            if (string_Nectarines != null && !string_Nectarines.isEmpty())
            {
                textView_Nectarines.setVisibility(View.VISIBLE);
                linearLayout_Nectarines.setVisibility(View.VISIBLE);
            }

            string_Oranges = extras.getString("string_Oranges");
            if (string_Oranges != null && !string_Oranges.isEmpty())
            {
                textView_Oranges.setVisibility(View.VISIBLE);
                linearLayout_Oranges.setVisibility(View.VISIBLE);
            }

            string_Pears = extras.getString("string_Pears");
            if (string_Pears != null && !string_Pears.isEmpty())
            {
                textView_Pears.setVisibility(View.VISIBLE);
                linearLayout_Pears.setVisibility(View.VISIBLE);
            }

        }

        //Changing products counter.

        button_Plus_Carrots.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                carrots_Counter++;

                if (carrots_Counter >= 100)
                {
                    carrots_Counter = 100;
                }
                displayCarrotsCounter(carrots_Counter);
            }
        });

        button_Plus_Cauliflower.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                cauliflower_Counter++;

                if (cauliflower_Counter >= 100)
                {
                    cauliflower_Counter = 100;
                    Toast.makeText(TotalSettings.this,toast_MaxCounter , Toast.LENGTH_SHORT).show();
                }
                displayCauliflowerCounter(cauliflower_Counter);
            }
        });

        button_Plus_Cucumbers.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                cucumbers_Counter++;

                if (cucumbers_Counter >= 100)
                {
                    cucumbers_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayCucumbersCounter(cucumbers_Counter);
            }
        });

        button_Plus_Broccoli.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                broccoli_Counter++;

                if (broccoli_Counter >= 100)
                {
                    broccoli_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayBroccoliCounter(broccoli_Counter);
            }
        });


        button_Plus_Potatoes.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                potatoes_Counter++;

                if (potatoes_Counter >= 100)
                {
                    potatoes_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayPotatoesCounter(potatoes_Counter);
            }
        });


        button_Plus_Spinach.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                spinach_Counter++;

                if (spinach_Counter >= 100)
                {
                    spinach_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displaySpinachCounter(spinach_Counter);
            }
        });

        button_Plus_Tomatoes.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                tomatoes_Counter++;

                if (tomatoes_Counter >= 100)
                {
                    tomatoes_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayTomatoesCounter(tomatoes_Counter);
            }
        });

        button_Plus_Onion.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                onion_Counter++;

                if (onion_Counter >= 100)
                {
                    onion_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayOnionCounter(onion_Counter);
            }
        });

        button_Plus_Pumpkins.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                pumpkins_Counter++;

                if (pumpkins_Counter >= 100)
                {
                    pumpkins_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayPumpkinsCounter(pumpkins_Counter);
            }
        });

        button_Plus_Peas.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                peas_Counter++;

                if (peas_Counter >= 100)
                {
                    peas_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayPeasCounter(peas_Counter);
            }
        });

        button_Plus_Garlic.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                garlic_Counter++;

                if (garlic_Counter >= 100)
                {
                    garlic_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayGarlicCounter(garlic_Counter);
            }
        });

        button_Plus_Mushrooms.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                mushrooms_Counter++;

                if (mushrooms_Counter >= 100)
                {
                    mushrooms_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayMushroomsCounter(mushrooms_Counter);
            }
        });

        button_Minus_Carrots.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                carrots_Counter--;

                if (carrots_Counter < checkLowAm)
                {
                    carrots_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayCarrotsCounter(carrots_Counter);
            }
        });


        button_Minus_Cauliflower.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                cauliflower_Counter--;

                if (cauliflower_Counter < checkLowAm)
                {
                    cauliflower_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayCauliflowerCounter(cauliflower_Counter);
            }
        });

        button_Minus_Cucumbers.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                cucumbers_Counter--;

                if (cucumbers_Counter < checkLowAm)
                {
                    cucumbers_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayCucumbersCounter(cucumbers_Counter);
            }
        });

        button_Minus_Broccoli.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                broccoli_Counter--;

                if (broccoli_Counter < checkLowAm)
                {
                    broccoli_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayBroccoliCounter(broccoli_Counter);
            }
        });


        button_Minus_Potatoes.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                potatoes_Counter--;

                if (potatoes_Counter < checkLowAm)
                {
                    potatoes_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayPotatoesCounter(potatoes_Counter);
            }
        });


        button_Minus_Spinach.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v
            ) {
                spinach_Counter--;

                if (spinach_Counter < checkLowAm)
                {
                    spinach_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displaySpinachCounter(spinach_Counter);
            }
        });

        button_Minus_Tomatoes.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                tomatoes_Counter--;

                if (tomatoes_Counter < checkLowAm)
                {
                    tomatoes_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayTomatoesCounter(tomatoes_Counter);
            }
        });

        button_Minus_Onion.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                onion_Counter--;

                if (onion_Counter < checkLowAm)
                {
                    onion_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayOnionCounter(onion_Counter);
            }
        });

        button_Minus_Pumpkins.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                pumpkins_Counter--;

                if (pumpkins_Counter < checkLowAm)
                {
                    pumpkins_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayPumpkinsCounter(pumpkins_Counter);
            }
        });

        button_Minus_Peas.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                peas_Counter--;

                if (peas_Counter < checkLowAm)
                {
                    peas_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayPeasCounter(peas_Counter);
            }
        });

        button_Minus_Garlic.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                garlic_Counter--;

                if (garlic_Counter < checkLowAm)
                {
                    garlic_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayGarlicCounter(garlic_Counter);
            }
        });

        button_Minus_Mushrooms.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                mushrooms_Counter--;

                if (mushrooms_Counter < checkLowAm)
                {
                    mushrooms_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayMushroomsCounter(mushrooms_Counter);
            }
        });

        button_Plus_Apples.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                apples_Counter++;

                if (apples_Counter >= 100)
                {
                    apples_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayApplesCounter(apples_Counter);
            }
        });

        button_Plus_Bananas.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                bananas_Counter++;

                if (bananas_Counter >= 100)
                {
                    bananas_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayBananasCounter(bananas_Counter);
            }
        });

        button_Plus_Pineapples.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                pineapples_Counter++;

                if (pineapples_Counter >= 100)
                {
                    pineapples_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayPineapplesCounter(pineapples_Counter);
            }
        });

        button_Plus_Strawberries.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                strawberries_Counter++;

                if (strawberries_Counter >= 100)
                {
                    strawberries_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayStrawberriesCounter(strawberries_Counter);
            }
        });


        button_Plus_Watermelons.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                watermelons_Counter++;

                if (watermelons_Counter >= 100)
                {
                    watermelons_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayWatermelonsCounter(watermelons_Counter);
            }
        });


        button_Plus_Limes.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                limes_Counter++;

                if (limes_Counter >= 100)
                {
                    limes_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayLimesCounter(limes_Counter);
            }
        });

        button_Plus_Lemons.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                lemons_Counter++;

                if (lemons_Counter >= 100)
                {
                    lemons_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayLemonsCounter(lemons_Counter);
            }
        });

        button_Plus_JavaPlums.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                javaPlums_Counter++;

                if (javaPlums_Counter >= 100)
                {
                    javaPlums_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayJavaPlumsCounter(javaPlums_Counter);
            }
        });

        button_Plus_Mangos.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                mangos_Counter++;

                if (mangos_Counter >= 100)
                {
                    mangos_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayMangosCounter(mangos_Counter);
            }
        });

        button_Plus_Nectarines.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                nectarines_Counter++;

                if (nectarines_Counter >= 100)
                {
                    nectarines_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayNectarinesCounter(nectarines_Counter);
            }
        });

        button_Plus_Oranges.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                oranges_Counter++;

                if (oranges_Counter >= 100)
                {
                    oranges_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayOrangesCounter(oranges_Counter);
            }
        });

        button_Plus_Pears.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                pears_Counter++;

                if (pears_Counter >= 100)
                {
                    pears_Counter = 100;
                    Toast.makeText(TotalSettings.this, toast_MaxCounter, Toast.LENGTH_SHORT).show();
                }
                displayPearsCounter(pears_Counter);
            }
        });

        button_Minus_Apples.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                apples_Counter--;

                if (apples_Counter < checkLowAm)
                {
                    apples_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayApplesCounter(apples_Counter);
            }
        });

        button_Minus_Bananas.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                bananas_Counter--;

                if (bananas_Counter < checkLowAm)
                {
                    bananas_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayBananasCounter(bananas_Counter);
            }
        });

        button_Minus_Pineapples.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                pineapples_Counter--;

                if (pineapples_Counter < checkLowAm)
                {
                    pineapples_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayPineapplesCounter(pineapples_Counter);
            }
        });

        button_Minus_Strawberries.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                strawberries_Counter--;

                if (strawberries_Counter < checkLowAm)
                {
                    strawberries_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayStrawberriesCounter(strawberries_Counter);
            }
        });


        button_Minus_Watermelons.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                watermelons_Counter--;

                if (watermelons_Counter < checkLowAm)
                {
                    watermelons_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayWatermelonsCounter(watermelons_Counter);
            }
        });


        button_Minus_Limes.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                limes_Counter--;

                if (limes_Counter < checkLowAm)
                {
                    limes_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayLimesCounter(limes_Counter);
            }
        });

        button_Minus_Lemons.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                lemons_Counter--;

                if (lemons_Counter < checkLowAm)
                {
                    lemons_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayLemonsCounter(lemons_Counter);
            }
        });

        button_Minus_JavaPlums.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                javaPlums_Counter--;

                if (javaPlums_Counter < checkLowAm)
                {
                    javaPlums_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayJavaPlumsCounter(javaPlums_Counter);
            }
        });

        button_Minus_Mangos.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                mangos_Counter--;

                if (mangos_Counter < checkLowAm)
                {
                    mangos_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayMangosCounter(mangos_Counter);
            }
        });

        button_Minus_Nectarines.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                nectarines_Counter--;

                if (nectarines_Counter < checkLowAm)
                {
                    nectarines_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayNectarinesCounter(nectarines_Counter);
            }
        });

        button_Minus_Oranges.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                oranges_Counter--;

                if (oranges_Counter < checkLowAm)
                {
                    oranges_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayOrangesCounter(oranges_Counter);
            }
        });

        button_Minus_Pears.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                pears_Counter--;

                if (pears_Counter < checkLowAm)
                {
                    pears_Counter = checkLowAm;
                    Toast.makeText(TotalSettings.this, toast_MinCounter, Toast.LENGTH_SHORT).show();
                }
                displayPearsCounter(pears_Counter);
            }
        });

        button_Order.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                if(total_sum != 0 && checkSubmitButton)
                {
                    checkSubmitButton = false;
                    String totalSum_Text = "Your sum is: " + sumFormat.format(total_sum);

                    String string_CarrotsCounter = valueOf(carrots_Counter);
                    String carrotsCounter_Text = "Your carrots counter is: " + string_CarrotsCounter;

                    String string_CauliflowerCounter = valueOf(cauliflower_Counter);
                    String cauliflowerCounter_Text = "Your cauliflower counter is: " + string_CauliflowerCounter;

                    String string_CucumbersCounter = valueOf(cucumbers_Counter);
                    String cucumbersCounter_Text = "Your cucumbers counter is: " + string_CucumbersCounter;

                    String string_BroccoliCounter = valueOf(broccoli_Counter);
                    String broccoliCounter_Text = "Your broccoli counter is: " + string_BroccoliCounter;

                    String string_PotatoesCounter = valueOf(potatoes_Counter);
                    String potatoesCounter_Text = "Your potatoes counter is: " + string_PotatoesCounter;

                    String string_SpinachCounter = valueOf(spinach_Counter);
                    String spinachCounter_Text = "Your spinach counter is: " + string_SpinachCounter;

                    String string_TomatoesCounter = valueOf(tomatoes_Counter);
                    String tomatoesCounter_Text = "Your tomatoes counter is: " + string_TomatoesCounter;

                    String string_OnionCounter = valueOf(onion_Counter);
                    String onionCounter_Text = "Your onion counter is: " + string_OnionCounter;

                    String string_PumpkinsCounter = valueOf(pumpkins_Counter);
                    String pumpkinsCounter_Text = "Your pumpkins counter is: " + string_PumpkinsCounter;

                    String string_PeasCounter = valueOf(peas_Counter);
                    String peasCounter_Text = "Your peas counter is: " + string_PeasCounter;

                    String string_GarlicCounter = valueOf(garlic_Counter);
                    String garlicCounter_Text = "Your garlic counter is: " + string_GarlicCounter;

                    String string_MushroomsCounter = valueOf(mushrooms_Counter);
                    String mushroomsCounter_Text = "Your mushrooms counter is: " + string_MushroomsCounter;

                    String string_ApplesCounter = valueOf(apples_Counter);
                    String applesCounter_Text = "Your apples counter is: " + string_ApplesCounter;

                    String string_BananasCounter = valueOf(bananas_Counter);
                    String bananasCounter_Text = "Your bananas counter is: " + string_BananasCounter;

                    String string_PineapplesCounter = valueOf(pineapples_Counter);
                    String pineapplesCounter_Text = "Your pineapples counter is: " + string_PineapplesCounter;

                    String string_StrawberriesCounter = valueOf(strawberries_Counter);
                    String strawberriesCounter_Text = "Your strawberries counter is: " + string_StrawberriesCounter;

                    String string_WatermelonsCounter = valueOf(watermelons_Counter);
                    String watermelonsCounter_Text = "Your watermelons counter is: " + string_WatermelonsCounter;

                    String string_LimesCounter = valueOf(limes_Counter);
                    String limesCounter_Text = "Your limes counter is: " + string_LimesCounter;

                    String string_LemonsCounter = valueOf(lemons_Counter);
                    String lemonsCounter_Text = "Your lemons counter is: " + string_LemonsCounter;

                    String string_javaPlumsCounter = valueOf(javaPlums_Counter);
                    String javaPlumsCounter_Text = "Your java-plums counter is: " + string_javaPlumsCounter;

                    String string_MangosCounter = valueOf(mangos_Counter);
                    String mangosCounter_Text = "Your mangos counter is: " + string_MangosCounter;

                    String string_NectarinesCounter = valueOf(nectarines_Counter);
                    String nectarinesCounter_Text = "Your nectarines counter is: " + string_NectarinesCounter;

                    String string_OrangesCounter = valueOf(oranges_Counter);
                    String orangesCounter_Text = "Your oranges counter is: " + string_OrangesCounter;

                    String string_PearsCounter = valueOf(pears_Counter);
                    String pearsCounter_Text = "Your pears counter is: " + string_PearsCounter;

                    emailText = totalSum_Text + " лв.";

                    Bundle extras = getIntent().getExtras();
                    if (extras != null) {

                        string_Carrots = extras.getString("string_Carrots");
                        if (string_Carrots != null && !string_Carrots.isEmpty())
                        {
                            emailText += "\n" + carrotsCounter_Text + kg;
                        }

                        string_Cauliflower = extras.getString("string_Cauliflower");
                        if (string_Cauliflower != null && !string_Cauliflower.isEmpty())
                        {
                            emailText += "\n" + cauliflowerCounter_Text + kg;
                        }

                        string_Cucumbers = extras.getString("string_Cucumbers");
                        if (string_Cucumbers != null && !string_Cucumbers.isEmpty())
                        {
                            emailText += "\n" + cucumbersCounter_Text + kg;
                        }

                        string_Broccoli = extras.getString("string_Broccoli");
                        if (string_Broccoli != null && !string_Broccoli.isEmpty())
                        {
                            emailText += "\n" + broccoliCounter_Text + kg;
                        }

                        string_Potatoes = extras.getString("string_Potatoes");
                        if (string_Potatoes != null && !string_Potatoes.isEmpty())
                        {
                            emailText += "\n" + potatoesCounter_Text + kg;
                        }

                        string_Spinach = extras.getString("string_Spinach");
                        if (string_Spinach != null && !string_Spinach.isEmpty())
                        {
                            emailText += "\n" + spinachCounter_Text + kg;
                        }

                        string_Tomatoes = extras.getString("string_Tomatoes");
                        if (string_Tomatoes != null && !string_Tomatoes.isEmpty())
                        {
                            emailText += "\n" + tomatoesCounter_Text + kg;
                        }

                        string_Onions = extras.getString("string_Onions");
                        if (string_Onions != null && !string_Onions.isEmpty())
                        {
                            emailText += "\n" + onionCounter_Text + kg;
                        }

                        string_Pumpkin = extras.getString("string_Pumpkin");
                        if (string_Pumpkin != null && !string_Pumpkin.isEmpty())
                        {
                            emailText += "\n" + pumpkinsCounter_Text + kg;
                        }

                        string_Peas = extras.getString("string_Peas");
                        if (string_Peas != null && !string_Peas.isEmpty())
                        {
                            emailText += "\n" + peasCounter_Text + kg;
                        }

                        string_Garlic = extras.getString("string_Garlic");
                        if (string_Garlic != null && !string_Garlic.isEmpty())
                        {
                            emailText += "\n" + garlicCounter_Text + kg;
                        }

                        string_Mushrooms = extras.getString("string_Mushrooms");
                        if (string_Mushrooms != null && !string_Mushrooms.isEmpty())
                        {
                            emailText += "\n" + mushroomsCounter_Text + kg;
                        }

                        string_Apples = extras.getString("string_Apples");
                        if (string_Apples != null && !string_Apples.isEmpty())
                        {
                            emailText += "\n" + applesCounter_Text + kg;
                        }

                        string_Bananas = extras.getString("string_Bananas");
                        if (string_Bananas != null && !string_Bananas.isEmpty())
                        {
                            emailText += "\n" + bananasCounter_Text + kg;
                        }

                        string_Pineapples = extras.getString("string_Pineapples");
                        if (string_Pineapples != null && !string_Pineapples.isEmpty())
                        {
                            emailText += "\n" + pineapplesCounter_Text + kg;
                        }

                        string_Strawberries = extras.getString("string_Strawberries");
                        if (string_Strawberries != null && !string_Strawberries.isEmpty())
                        {
                            emailText += "\n" + strawberriesCounter_Text + kg;
                        }

                        string_Watermelons = extras.getString("string_Watermelons");
                        if (string_Watermelons != null && !string_Watermelons.isEmpty())
                        {
                            emailText += "\n" + watermelonsCounter_Text + kg;
                        }

                        string_Limes = extras.getString("string_Limes");
                        if (string_Limes != null && !string_Limes.isEmpty())
                        {
                            emailText += "\n" + limesCounter_Text + kg;
                        }

                        string_Lemons = extras.getString("string_Lemons");
                        if (string_Lemons != null && !string_Lemons.isEmpty())
                        {
                            emailText += "\n" + lemonsCounter_Text + kg;
                        }

                        string_JavaPlums = extras.getString("string_JavaPlums");
                        if (string_JavaPlums != null && !string_JavaPlums.isEmpty())
                        {
                            emailText += "\n" + javaPlumsCounter_Text + kg;
                        }

                        string_Mangos = extras.getString("string_Mangos");
                        if (string_Mangos != null && !string_Mangos.isEmpty())
                        {
                            emailText += "\n" + mangosCounter_Text + kg;
                        }

                        string_Nectarines = extras.getString("string_Nectarines");
                        if (string_Nectarines != null && !string_Nectarines.isEmpty())
                        {
                            emailText += "\n" + nectarinesCounter_Text + kg;
                        }

                        string_Oranges = extras.getString("string_Oranges");
                        if (string_Oranges != null && !string_Oranges.isEmpty())
                        {
                            emailText += "\n" + orangesCounter_Text + kg;
                        }

                        string_Pears = extras.getString("string_Pears");
                        if (string_Pears != null && !string_Pears.isEmpty())
                        {
                            emailText += "\n" + pearsCounter_Text + kg;
                        }
                    }

                    Intent intentSendEmail = new Intent(Intent.ACTION_SENDTO);
                    intentSendEmail.setData(Uri.parse("mailto:"));
                    intentSendEmail.putExtra(Intent.EXTRA_EMAIL, new String[]{"parvanovski_ivan@abv.bg"});
                    intentSendEmail.putExtra(Intent.EXTRA_SUBJECT, "Grocery Order!");
                    intentSendEmail.putExtra(Intent.EXTRA_TEXT, emailText);


                    if (intentSendEmail.resolveActivity(getPackageManager()) != null) {
                        startActivity(intentSendEmail);
                    }
                }else
                {
                    Toast.makeText(TotalSettings.this,"Please SUBMIT YOUR ORDER", Toast.LENGTH_SHORT).show();                    }
            }

        });

        button_PreviousMenu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intentBack = new Intent(TotalSettings.this, Mix_Products.class);
                startActivity(intentBack);
            }
        });


        //Calculating the sum.

        button_Submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                checkSubmitButton = true;
                if (string_Carrots != null && !string_Carrots.isEmpty())
                {
                    carrots_sum = carrots_Counter * carrots_price;
                }

                if (string_Cauliflower != null && !string_Cauliflower.isEmpty())
                {
                    cauliflower_sum = cauliflower_Counter * cauliflower_price;
                }

                if (string_Cucumbers != null && !string_Cucumbers.isEmpty())
                {
                    cucumbers_sum = cucumbers_Counter * cucumbers_price;
                }

                if (string_Broccoli != null && !string_Broccoli.isEmpty())
                {
                    broccoli_sum = broccoli_Counter * broccoli_price;
                }

                if (string_Potatoes != null && !string_Potatoes.isEmpty())
                {
                    potatoes_sum = potatoes_Counter * potatoes_price;
                }

                if (string_Spinach != null && !string_Spinach.isEmpty())
                {
                    spinach_sum = spinach_Counter * spinach_price;
                }

                if (string_Tomatoes != null && !string_Tomatoes.isEmpty())
                {
                    tomatoes_sum = tomatoes_Counter * tomatoes_price;
                }

                if (string_Onions != null && !string_Onions.isEmpty())
                {
                    onion_sum = onion_Counter * onion_price;
                }

                if (string_Pumpkin != null && !string_Pumpkin.isEmpty())
                {
                    pumpkins_sum = pumpkins_Counter * pumpkins_price;
                }

                if (string_Peas != null && !string_Peas.isEmpty())
                {
                    peas_sum = peas_Counter * peas_price;
                }

                if (string_Garlic != null && !string_Garlic.isEmpty())
                {
                    garlic_sum = garlic_Counter * garlic_price;
                }

                if (string_Mushrooms != null && !string_Mushrooms.isEmpty())
                {
                    mushrooms_sum = mushrooms_Counter * mushrooms_price;
                }

                if (string_Apples != null && !string_Apples.isEmpty())
                {
                    apples_sum = apples_Counter * apples_price;
                }

                if (string_Bananas != null && !string_Bananas.isEmpty())
                {
                    bananas_sum = bananas_Counter * bananas_price;
                }

                if (string_Pineapples != null && !string_Pineapples.isEmpty())
                {
                    pineapple_sum = pineapples_Counter * pineapples_price;
                }

                if (string_Strawberries != null && !string_Strawberries.isEmpty())
                {
                    strawberries_sum = strawberries_Counter * strawberries_price;
                }

                if (string_Watermelons != null && !string_Watermelons.isEmpty())
                {
                    watermelons_sum = watermelons_Counter * watermelons_price;
                }

                if (string_Limes != null && !string_Limes.isEmpty())
                {
                    limes_sum = limes_Counter * limes_price;
                }

                if (string_Lemons != null && !string_Lemons.isEmpty())
                {
                    lemons_sum = lemons_Counter * lemons_price;
                }

                if (string_JavaPlums != null && !string_JavaPlums.isEmpty())
                {
                    javaplums_sum = javaPlums_Counter * javaPlums_price;
                }

                if (string_Mangos != null && !string_Mangos.isEmpty())
                {
                    mangos_sum = mangos_Counter * mangos_price;
                }

                if (string_Nectarines != null && !string_Nectarines.isEmpty())
                {
                    nectarines_sum = nectarines_Counter * nectarines_price;
                }

                if (string_Oranges != null && !string_Oranges.isEmpty())
                {
                    oranges_sum = oranges_Counter * oranges_price;
                }

                if (string_Pears != null && !string_Pears.isEmpty())
                {
                    pears_sum = pears_Counter * pears_price;
                }

                total_sum = apples_sum + bananas_sum + pineapple_sum + strawberries_sum + watermelons_sum + limes_sum + lemons_sum + javaplums_sum + mangos_sum + nectarines_sum + oranges_sum + pears_sum + carrots_sum + cauliflower_sum + cucumbers_sum + broccoli_sum + potatoes_sum + spinach_sum + tomatoes_sum + onion_sum + pumpkins_sum + peas_sum + garlic_sum + mushrooms_sum;
                displayFullSum(total_sum);

            }
        });

    }

    public void errorFix(View view) {}


    //Set the products counter and Total Sum.

    private void displayFullSum(double total_sum)
    {
        textView_TotalNumber.setText(NumberFormat.getCurrencyInstance().format(total_sum));
    }

    private void displayCarrotsCounter(int carrots_Counter)
    {
        String string_Counter_Carrots = String.valueOf(carrots_Counter);
        textView_Counter_Carrots.setText(string_Counter_Carrots);
    }

    private void displayCauliflowerCounter(int cauliflower_Counter)
    {
        String string_Counter_Cauliflower = String.valueOf(cauliflower_Counter);
        textView_Counter_Cauliflower.setText(string_Counter_Cauliflower);
    }

    private void displayCucumbersCounter(int cucumbers_Counter)
    {
        String string_Counter_Cucumbers = String.valueOf(cucumbers_Counter);
        textView_Counter_Cucumbers.setText(string_Counter_Cucumbers);
    }

    private void displayBroccoliCounter(int broccoli_Counter)
    {
        String string_Counter_Broccoli = String.valueOf(broccoli_Counter);
        textView_Counter_Broccoli.setText(string_Counter_Broccoli);
    }

    private void displayPotatoesCounter(int potatoes_Counter)
    {
        String string_Counter_Potatoes = String.valueOf(potatoes_Counter);
        textView_Counter_Potatoes.setText(string_Counter_Potatoes);
    }

    private void displaySpinachCounter(int spinach_Counter)
    {
        String string_Counter_Spinach = String.valueOf(spinach_Counter);
        textView_Counter_Spinach.setText(string_Counter_Spinach);
    }

    private void displayTomatoesCounter(int tomatoes_Counter)
    {
        String string_Counter_Tomatoes = String.valueOf(tomatoes_Counter);
        textView_Counter_Tomatoes.setText(string_Counter_Tomatoes);
    }

    private void displayOnionCounter(int onion_Counter)
    {
        String string_Counter_Onion = String.valueOf(onion_Counter);
        textView_Counter_Onion.setText(string_Counter_Onion);
    }

    private void displayPumpkinsCounter(int pumpkins_Counter)
    {
        String string_Counter_Pumpkins = String.valueOf(pumpkins_Counter);
        textView_Counter_Pumpkins.setText(string_Counter_Pumpkins);
    }

    private void displayPeasCounter(int peas_Counter)
    {
        String string_Counter_Peas = String.valueOf(peas_Counter);
        textView_Counter_Peas.setText(string_Counter_Peas);
    }

    private void displayGarlicCounter(int garlic_Counter)
    {
        String string_Counter_Garlic = String.valueOf(garlic_Counter);
        textView_Counter_Garlic.setText(string_Counter_Garlic);
    }

    private void displayMushroomsCounter(int mushrooms_Counter)
    {
        String string_Counter_Mushrooms = String.valueOf(mushrooms_Counter);
        textView_Counter_Mushrooms.setText(string_Counter_Mushrooms);
    }

    private void displayApplesCounter(int apples_Counter)
    {
        String string_Counter_Apples = String.valueOf(apples_Counter);
        textView_Counter_Apples.setText(string_Counter_Apples);
    }

    private void displayBananasCounter(int bananas_Counter)
    {
        String string_Counter_Bananas = String.valueOf(bananas_Counter);
        textView_Counter_Bananas.setText(string_Counter_Bananas);
    }

    private void displayPineapplesCounter(int pineapples_Counter)
    {
        String string_Counter_Pineapples = String.valueOf(pineapples_Counter);
        textView_Counter_Pineapples.setText(string_Counter_Pineapples);
    }

    private void displayStrawberriesCounter(int strawberries_Counter)
    {
        String string_Counter_Strawberries = String.valueOf(strawberries_Counter);
        textView_Counter_Strawberries.setText(string_Counter_Strawberries);
    }

    private void displayWatermelonsCounter(int watermelons_Counter)
    {
        String string_Counter_Watermelons = String.valueOf(watermelons_Counter);
        textView_Counter_Watermelons.setText(string_Counter_Watermelons);
    }

    private void displayLimesCounter(int limes_Counter)
    {
        String string_Counter_Limes = String.valueOf(limes_Counter);
        textView_Counter_Limes.setText(string_Counter_Limes);
    }

    private void displayLemonsCounter(int lemons_Counter)
    {
        String string_Counter_Lemons = String.valueOf(lemons_Counter);
        textView_Counter_Lemons.setText(string_Counter_Lemons);
    }

    private void displayJavaPlumsCounter(int javaPlums_Counter)
    {
        String string_Counter_JavaPlums = String.valueOf(javaPlums_Counter);
        textView_Counter_JavaPlums.setText(string_Counter_JavaPlums);
    }

    private void displayMangosCounter(int mangos_Counter)
    {
        String string_Counter_Mangos = String.valueOf(mangos_Counter);
        textView_Counter_Mangos.setText(string_Counter_Mangos);
    }

    private void displayNectarinesCounter(int nectarines_Counter)
    {
        String string_Counter_Nectarines = String.valueOf(nectarines_Counter);
        textView_Counter_Nectarines.setText(string_Counter_Nectarines);
    }

    private void displayOrangesCounter(int oranges_Counter)
    {
        String string_Counter_Oranges = String.valueOf(oranges_Counter);
        textView_Counter_Oranges.setText(string_Counter_Oranges);
    }

    private void displayPearsCounter(int pears_Counter)
    {
        String string_Counter_Pears = String.valueOf(pears_Counter);
        textView_Counter_Pears.setText(string_Counter_Pears);
    }

    //Saving and Restoring Information.
    @Override
    public void onSaveInstanceState(Bundle savedInstanceState)
    {
        savedInstanceState.putDouble("total_sum", total_sum);

        savedInstanceState.putInt("apples_Counter", apples_Counter);
        savedInstanceState.putInt("bananas_Counter", bananas_Counter);
        savedInstanceState.putInt("pineapples_Counter", pineapples_Counter);
        savedInstanceState.putInt("strawberries_Counter", strawberries_Counter);
        savedInstanceState.putInt("watermelons_Counter", watermelons_Counter);
        savedInstanceState.putInt("limes_Counter", limes_Counter);
        savedInstanceState.putInt("lemons_Counter", lemons_Counter);
        savedInstanceState.putInt("javaPlums_Counter", javaPlums_Counter);
        savedInstanceState.putInt("mangos_Counter", mangos_Counter);
        savedInstanceState.putInt("nectarines_Counter", nectarines_Counter);
        savedInstanceState.putInt("oranges_Counter", oranges_Counter);
        savedInstanceState.putInt("pears_Counter", pears_Counter);

        savedInstanceState.putInt("carrots_Counter", carrots_Counter);
        savedInstanceState.putInt("cauliflower_Counter", cauliflower_Counter);
        savedInstanceState.putInt("cucumbers_Counter", cucumbers_Counter);
        savedInstanceState.putInt("broccoli_Counter", broccoli_Counter);
        savedInstanceState.putInt("potatoes_Counter", potatoes_Counter);
        savedInstanceState.putInt("spinach_Counter", spinach_Counter);
        savedInstanceState.putInt("tomatoes_Counter", tomatoes_Counter);
        savedInstanceState.putInt("onion_Counter", onion_Counter);
        savedInstanceState.putInt("pumpkins_Counter", pumpkins_Counter);
        savedInstanceState.putInt("peas_Counter", peas_Counter);
        savedInstanceState.putInt("garlic_Counter", garlic_Counter);
        savedInstanceState.putInt("mushrooms_Counter", mushrooms_Counter);
        savedInstanceState.putBoolean("checkSubmitButton", checkSubmitButton);
        super.onSaveInstanceState(savedInstanceState);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState)
    {
        total_sum = savedInstanceState.getDouble("total_sum");
        apples_Counter = savedInstanceState.getInt("apples_Counter");
        bananas_Counter = savedInstanceState.getInt("bananas_Counter");
        pineapples_Counter = savedInstanceState.getInt("pineapples_Counter");
        strawberries_Counter = savedInstanceState.getInt("strawberries_Counter");
        watermelons_Counter = savedInstanceState.getInt("watermelons_Counter");
        limes_Counter = savedInstanceState.getInt("limes_Counter");
        lemons_Counter = savedInstanceState.getInt("lemons_Counter");
        javaPlums_Counter = savedInstanceState.getInt("javaPlums_Counter");
        mangos_Counter = savedInstanceState.getInt("mangos_Counter");
        nectarines_Counter = savedInstanceState.getInt("nectarines_Counter");
        oranges_Counter = savedInstanceState.getInt("oranges_Counter");
        pears_Counter = savedInstanceState.getInt("pears_Counter");

        carrots_Counter = savedInstanceState.getInt("carrots_Counter");
        cauliflower_Counter = savedInstanceState.getInt("cauliflower_Counter");
        cucumbers_Counter = savedInstanceState.getInt("cucumbers_Counter");
        broccoli_Counter = savedInstanceState.getInt("broccoli_Counter");
        potatoes_Counter = savedInstanceState.getInt("potatoes_Counter");
        spinach_Counter = savedInstanceState.getInt("spinach_Counter");
        tomatoes_Counter = savedInstanceState.getInt("tomatoes_Counter");
        onion_Counter = savedInstanceState.getInt("onion_Counter");
        pumpkins_Counter = savedInstanceState.getInt("pumpkins_Counter");
        peas_Counter = savedInstanceState.getInt("peas_Counter");
        garlic_Counter = savedInstanceState.getInt("garlic_Counter");
        mushrooms_Counter = savedInstanceState.getInt("mushrooms_Counter");
        checkSubmitButton = savedInstanceState.getBoolean("checkSubmitButton");


        textView_TotalNumber.setText(NumberFormat.getCurrencyInstance().format(total_sum));
        textView_Counter_Apples.setText(String.valueOf(apples_Counter));
        textView_Counter_Bananas.setText(String.valueOf(bananas_Counter));
        textView_Counter_Pineapples.setText(String.valueOf(pineapples_Counter));
        textView_Counter_Strawberries.setText(String.valueOf(strawberries_Counter));
        textView_Counter_Watermelons.setText(String.valueOf(watermelons_Counter));
        textView_Counter_Limes.setText(String.valueOf(limes_Counter));
        textView_Counter_Lemons.setText(String.valueOf(lemons_Counter));
        textView_Counter_JavaPlums.setText(String.valueOf(javaPlums_Counter));
        textView_Counter_Mangos.setText(String.valueOf(mangos_Counter));
        textView_Counter_Nectarines.setText(String.valueOf(nectarines_Counter));
        textView_Counter_Oranges.setText(String.valueOf(oranges_Counter));
        textView_Counter_Pears.setText(String.valueOf(pears_Counter));

        textView_Counter_Carrots.setText(String.valueOf(carrots_Counter));
        textView_Counter_Cauliflower.setText(String.valueOf(cauliflower_Counter));
        textView_Counter_Cucumbers.setText(String.valueOf(cucumbers_Counter));
        textView_Counter_Broccoli.setText(String.valueOf(broccoli_Counter));
        textView_Counter_Potatoes.setText(String.valueOf(potatoes_Counter));
        textView_Counter_Spinach.setText(String.valueOf(spinach_Counter));
        textView_Counter_Tomatoes.setText(String.valueOf(tomatoes_Counter));
        textView_Counter_Onion.setText(String.valueOf(onion_Counter));
        textView_Counter_Pumpkins.setText(String.valueOf(pumpkins_Counter));
        textView_Counter_Peas.setText(String.valueOf(peas_Counter));
        textView_Counter_Garlic.setText(String.valueOf(garlic_Counter));
        textView_Counter_Mushrooms.setText(String.valueOf(mushrooms_Counter));
    }
}
