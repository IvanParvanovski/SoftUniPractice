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


public class Fruits_TotalSettings extends AppCompatActivity {

    LinearLayout linearLayout_Apples, linearLayout_Bananas, linearLayout_Pineapples, linearLayout_Strawberries;
    LinearLayout linearLayout_Watermelons, linearLayout_Limes, linearLayout_Lemons, linearLayout_JavaPlums;
    LinearLayout linearLayout_Mangos, linearLayout_Nectarines, linearLayout_Oranges, linearLayout_Pears;

    TextView textView_Apples, textView_Bananas, textView_Pineapples, textView_Strawberries;
    TextView textView_Watermelons, textView_Limes, textView_Lemons, textView_JavaPlums;
    TextView textView_Mangos, textView_Nectarines, textView_Oranges, textView_Pears;

    Button button_Plus_Apples, button_Plus_Bananas, button_Plus_Pineapples, button_Plus_Strawberries;
    Button button_Plus_Watermelons, button_Plus_Limes, button_Plus_Lemons, button_Plus_JavaPlums;
    Button button_Plus_Mangos, button_Plus_Nectarines, button_Plus_Oranges, button_Plus_Pears;
    Button button_Minus_Apples, button_Minus_Bananas, button_Minus_Pineapples, button_Minus_Strawberries;
    Button button_Minus_Watermelons, button_Minus_Limes, button_Minus_Lemons, button_Minus_JavaPlums;
    Button button_Minus_Mangos, button_Minus_Nectarines, button_Minus_Oranges, button_Minus_Pears;

    TextView textView_Counter_Apples, textView_Counter_Bananas, textView_Counter_Pineapples, textView_Counter_Strawberries;
    TextView textView_Counter_Watermelons, textView_Counter_Limes, textView_Counter_Lemons, textView_Counter_JavaPlums;
    TextView textView_Counter_Mangos, textView_Counter_Nectarines, textView_Counter_Oranges, textView_Counter_Pears;

    DecimalFormat sumFormat = new DecimalFormat("#.##");

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

    String emailText;
    String string_Apples, string_Bananas, string_Pineapples, string_Strawberries;
    String string_Watermelons, string_Limes, string_Lemons, string_JavaPlums;
    String string_Mangos, string_Nectarines, string_Oranges, string_Pears;

    Button button_PreviousMenu, button_Order, button_Submit;
    TextView textView_TotalNumber;

    double apples_sum, bananas_sum, pineapple_sum, strawberries_sum;
    double watermelons_sum, limes_sum, lemons_sum, javaplums_sum;
    double mangos_sum, nectarines_sum, oranges_sum, pears_sum;

    String kg = "kg.";


    double total_sum = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fruits__total_settings);

        button_PreviousMenu = findViewById(R.id.button_PreviousMenu);
        button_Order = findViewById(R.id.button_Order);
        button_Submit = findViewById(R.id.button_Submit);

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

        textView_TotalNumber = findViewById(R.id.textView_TotalNumber);



        //Checking if checkbox is checked and changing the visibility of our TextViews and Layouts.

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
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

        button_Plus_Apples.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v) {
                apples_Counter++;

                if (apples_Counter >= 100)
                {
                    apples_Counter = 100;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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

                if (apples_Counter < 1)
                {
                    apples_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (bananas_Counter < 1)
                {
                    bananas_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (pineapples_Counter < 1)
                {
                    pineapples_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (strawberries_Counter < 1)
                {
                    strawberries_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (watermelons_Counter < 1)
                {
                    watermelons_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (limes_Counter < 1)
                {
                    limes_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (lemons_Counter < 1)
                {
                    lemons_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (javaPlums_Counter < 1)
                {
                    javaPlums_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
                }
                displayJavaPlumsCounter(javaPlums_Counter);
            }
        });

        button_Minus_Mangos.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v) {
                mangos_Counter--;

                if (mangos_Counter < 1)
                {
                    mangos_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
                }
                displayMangosCounter(mangos_Counter);
            }
        });

        button_Minus_Nectarines.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v) {
                nectarines_Counter--;

                if (nectarines_Counter < 1)
                {
                    nectarines_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                if (oranges_Counter < 1)
                {
                    oranges_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (pears_Counter < 1)
                {
                    pears_Counter = 1;
                    Toast.makeText(Fruits_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
                }
                displayPearsCounter(pears_Counter);
            }
        });

        button_PreviousMenu.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intentBack = new Intent(Fruits_TotalSettings.this, Fruits.class);
                startActivity(intentBack);
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
                        Toast.makeText(Fruits_TotalSettings.this,"Please SUBMIT YOUR ORDER", Toast.LENGTH_SHORT).show();                    }
                    }

        });

        //Calculating the sum.

        button_Submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkSubmitButton = true;
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

                total_sum = apples_sum + bananas_sum + pineapple_sum + strawberries_sum + watermelons_sum + limes_sum + lemons_sum + javaplums_sum + mangos_sum + nectarines_sum + oranges_sum + pears_sum;
                displayFullSum(total_sum);
            }
        });

    }

    public void errorFix(View view){}

    //Set the products counter and Total Sum.

    private void displayFullSum(double total_sum)
    {
        textView_TotalNumber.setText(NumberFormat.getCurrencyInstance().format(total_sum));
    }

    private void displayApplesCounter(int apples_Counter)
    {
        String string_Counter_Apples = valueOf(apples_Counter);
        textView_Counter_Apples.setText(string_Counter_Apples);
    }

    private void displayBananasCounter(int bananas_Counter)
    {
        String string_Counter_Bananas = valueOf(bananas_Counter);
        textView_Counter_Bananas.setText(string_Counter_Bananas);
    }

    private void displayPineapplesCounter(int pineapples_Counter)
    {
        String string_Counter_Pineapples = valueOf(pineapples_Counter);
        textView_Counter_Pineapples.setText(string_Counter_Pineapples);
    }

    private void displayStrawberriesCounter(int strawberries_Counter)
    {
        String string_Counter_Strawberries = valueOf(strawberries_Counter);
        textView_Counter_Strawberries.setText(string_Counter_Strawberries);
    }

    private void displayWatermelonsCounter(int watermelons_Counter)
    {
        String string_Counter_Watermelons = valueOf(watermelons_Counter);
        textView_Counter_Watermelons.setText(string_Counter_Watermelons);
    }

    private void displayLimesCounter(int limes_Counter)
    {
        String string_Counter_Limes = valueOf(limes_Counter);
        textView_Counter_Limes.setText(string_Counter_Limes);
    }

    private void displayLemonsCounter(int lemons_Counter)
    {
        String string_Counter_Lemons = valueOf(lemons_Counter);
        textView_Counter_Lemons.setText(string_Counter_Lemons);
    }

    private void displayJavaPlumsCounter(int javaPlums_Counter)
    {
        String string_Counter_JavaPlums = valueOf(javaPlums_Counter);
        textView_Counter_JavaPlums.setText(string_Counter_JavaPlums);
    }

    private void displayMangosCounter(int mangos_Counter)
    {
        String string_Counter_Mangos = valueOf(mangos_Counter);
        textView_Counter_Mangos.setText(string_Counter_Mangos);
    }

    private void displayNectarinesCounter(int nectarines_Counter)
    {
        String string_Counter_Nectarines = valueOf(nectarines_Counter);
        textView_Counter_Nectarines.setText(string_Counter_Nectarines);
    }

    private void displayOrangesCounter(int oranges_Counter)
    {
        String string_Counter_Oranges = valueOf(oranges_Counter);
        textView_Counter_Oranges.setText(string_Counter_Oranges);
    }

    private void displayPearsCounter(int pears_Counter)
    {
        String string_Counter_Pears = valueOf(pears_Counter);
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
        checkSubmitButton = savedInstanceState.getBoolean("checkSubmitButton");

        textView_TotalNumber.setText(NumberFormat.getCurrencyInstance().format(total_sum));
        textView_Counter_Apples.setText(valueOf(apples_Counter));
        textView_Counter_Bananas.setText(valueOf(bananas_Counter));
        textView_Counter_Pineapples.setText(valueOf(pineapples_Counter));
        textView_Counter_Strawberries.setText(valueOf(strawberries_Counter));
        textView_Counter_Watermelons.setText(valueOf(watermelons_Counter));
        textView_Counter_Limes.setText(valueOf(limes_Counter));
        textView_Counter_Lemons.setText(valueOf(lemons_Counter));
        textView_Counter_JavaPlums.setText(valueOf(javaPlums_Counter));
        textView_Counter_Mangos.setText(valueOf(mangos_Counter));
        textView_Counter_Nectarines.setText(valueOf(nectarines_Counter));
        textView_Counter_Oranges.setText(valueOf(oranges_Counter));
        textView_Counter_Pears.setText(valueOf(pears_Counter));
    }

}
