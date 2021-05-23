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

public class Vegetables_TotalSettings extends AppCompatActivity {

    LinearLayout linearLayout_Carrots, linearLayout_Cauliflower, linearLayout_Cucumbers, linearLayout_Broccoli;
    LinearLayout linearLayout_Potatoes, linearLayout_Spinach, linearLayout_Tomatoes, linearLayout_Onion;
    LinearLayout linearLayout_Pumpkins, linearLayout_Peas, linearLayout_Garlic, linearLayout_Mushrooms;

    TextView textView_Carrots, textView_Cauliflower, textView_Cucumbers, textView_Broccoli;
    TextView textView_Potatoes, textView_Spinach, textView_Tomatoes, textView_Onion;
    TextView textView_Pumpkins, textView_Peas, textView_Garlic, textView_Mushrooms;

    String string_Carrots, string_Cauliflower, string_Cucumbers, string_Broccoli;
    String string_Potatoes, string_Spinach, string_Tomatoes, string_Onions;
    String string_Pumpkin, string_Peas, string_Garlic, string_Mushrooms;

    Button button_Plus_Carrots, button_Plus_Cauliflower, button_Plus_Cucumbers, button_Plus_Broccoli;
    Button button_Plus_Potatoes, button_Plus_Spinach, button_Plus_Tomatoes, button_Plus_Onion;
    Button button_Plus_Pumpkins, button_Plus_Peas, button_Plus_Garlic, button_Plus_Mushrooms;

    Button button_Minus_Carrots, button_Minus_Cauliflower, button_Minus_Cucumbers, button_Minus_Broccoli;
    Button button_Minus_Potatoes, button_Minus_Spinach, button_Minus_Tomatoes, button_Minus_Onion;
    Button button_Minus_Pumpkins, button_Minus_Peas, button_Minus_Garlic, button_Minus_Mushrooms;

    TextView textView_Counter_Carrots, textView_Counter_Cauliflower, textView_Counter_Cucumbers, textView_Counter_Broccoli;
    TextView textView_Counter_Potatoes, textView_Counter_Spinach, textView_Counter_Tomatoes, textView_Counter_Onion;
    TextView textView_Counter_Pumpkins, textView_Counter_Peas, textView_Counter_Garlic, textView_Counter_Mushrooms;


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
    boolean checkSubmitButton = false;

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

    Button button_Submit;
    Button button_Order;
    Button button_PreviousMenu;
    double total_sum = 0;
    TextView textView_TotalNumber;
    int checkLowAm = 1;
    String emailText;

    String kg = "kg.";

    DecimalFormat sumFormat = new DecimalFormat("#.##");

    double carrots_sum, cauliflower_sum, cucumbers_sum, broccoli_sum;
    double potatoes_sum, spinach_sum, tomatoes_sum, onion_sum;
    double pumpkins_sum, peas_sum, garlic_sum, mushrooms_sum;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_vegetables__total_settings);

        button_Submit = findViewById(R.id.button_Submit);
        textView_TotalNumber = findViewById(R.id.textView_TotalNumber);
        button_Order = findViewById(R.id.button_Order);

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

        button_PreviousMenu = findViewById(R.id.button_PreviousMenu);

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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате повече от 100kgs!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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

                if (potatoes_Counter < checkLowAm) {
                    potatoes_Counter = checkLowAm;
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
                }
                displayPotatoesCounter(potatoes_Counter);
            }
        });


        button_Minus_Spinach.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                spinach_Counter--;

                if (spinach_Counter < checkLowAm) {
                    spinach_Counter = checkLowAm;
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
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
                    Toast.makeText(Vegetables_TotalSettings.this, "Не можете да поръчате по-малко от 1kg!", Toast.LENGTH_SHORT).show();
                }
                displayMushroomsCounter(mushrooms_Counter);
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
                    Toast.makeText(Vegetables_TotalSettings.this,"Please SUBMIT YOUR ORDER", Toast.LENGTH_SHORT).show();                    }
            }

        });

        button_PreviousMenu.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intentBack = new Intent(Vegetables_TotalSettings.this, Vegetables.class);
                startActivity(intentBack);
            }
        });

        //Calculating the sum.

        button_Submit.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
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

                total_sum = carrots_sum + cauliflower_sum + cucumbers_sum + broccoli_sum + potatoes_sum + spinach_sum + tomatoes_sum + onion_sum + pumpkins_sum + peas_sum + garlic_sum + mushrooms_sum;
                displayFullSum(total_sum);

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

    //Saving and Restoring Information.
    @Override
    public void onSaveInstanceState(Bundle savedInstanceState)
    {
        savedInstanceState.putDouble("total_sum", total_sum);

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
