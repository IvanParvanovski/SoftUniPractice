package com.example.earthquake_app;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    ListView listView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


        setContentView(R.layout.activity_main);
        listView = findViewById(R.id.listView);

//        ArrayList<String> earthquakes = new ArrayList<>();
//        earthquakes.add("San Francisco");
//        earthquakes.add("London");
//        earthquakes.add("Tokyo");
//        earthquakes.add("Mexico City");
//        earthquakes.add("Moscow");
//        earthquakes.add("Rio de Janeiro");
//        earthquakes.add("Paris");

        ArrayList<EarthquakeModel> earthquakes = new ArrayList<>();
        earthquakes.add(new EarthquakeModel("7.2","San Francisco","Feb.2-2016"));
        earthquakes.add(new EarthquakeModel("6.1","London", "July 20-2015"));
        earthquakes.add(new EarthquakeModel("3.9","Tokyo", "Nov. 10-2014"));
        earthquakes.add(new EarthquakeModel("5.4","Mexico City", "Jan. 30-2013"));
        earthquakes.add(new EarthquakeModel("4.9","Moscow", "Aug. 19-2012"));
        earthquakes.add(new EarthquakeModel("7.2","Rio de Janeiro", "May 3-2013"));
        earthquakes.add(new EarthquakeModel("5.5","Paris", "Oct. 30-2011"));

        //ArrayAdapter<String> itemsAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, earthquakes);

        //We set our EarthquakeAdapter
        final EarthquakeAdapter adapter = new EarthquakeAdapter(this,earthquakes);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener(){
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){

            EarthquakeModel currentEarthquake = adapter.getItem(position);
            String itemLocation = String.valueOf(currentEarthquake.getmLocation());

            Toast.makeText(MainActivity.this, itemLocation, Toast.LENGTH_SHORT).show();
            }
        });

    }

}


