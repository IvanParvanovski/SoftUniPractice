package com.example.earthquake_app;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;

import java.util.List;

public class EarthquakeAdapter extends ArrayAdapter<EarthquakeModel> {

    public EarthquakeAdapter(@NonNull Context context, List<EarthquakeModel> earthquakes) {
        super(context,0, earthquakes);
    }

    //Override is to get something we need from a very big list of information
    @Override

    //We get the position
    public View getView(int position, View convertView, ViewGroup parent){

        View listItemView = convertView;

        //We check the listItemView if thre is nothing in it
        if (listItemView == null){
            listItemView = LayoutInflater.from(getContext()).inflate(R.layout.earthquake_list_item, parent, false);
        }

        //We make
        EarthquakeModel currentEarthquake = getItem(position);

        TextView magnitudeView = listItemView.findViewById(R.id.magnitude);
        magnitudeView.setText(currentEarthquake.getmMagnitude());

        TextView positionView = listItemView.findViewById(R.id.location);
        positionView.setText(currentEarthquake.getmLocation());

        TextView dateView = listItemView.findViewById(R.id.date);
        dateView.setText(currentEarthquake.getmDate());

        return listItemView;
    }

}


