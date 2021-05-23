package com.example.grocerystore.Adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.example.grocerystore.Model.Admin;
import com.example.grocerystore.R;

import java.util.ArrayList;

public class AdminAdapter extends  BaseAdapter{


    Context context;
    ArrayList<Admin> arrayList;
    public AdminAdapter(Context context, ArrayList<Admin> arrayList)
    {
        this.context=context;
        this.arrayList = arrayList;
    }

    @Override
    public int getCount() {
        return this.arrayList.size();
    }

    @Override
    public Object getItem(int position) {
        return arrayList.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

            LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            convertView = inflater.inflate(R.layout.admin_custom_listview, null);

            TextView textView_ID = convertView.findViewById(R.id.textView_ID);
            TextView textView_Username = convertView.findViewById(R.id.textView_Username);
            TextView textView_Password = convertView.findViewById(R.id.textView_Password);
            TextView textView_Address = convertView.findViewById(R.id.textView_Address);
            TextView textView_PopulatedPlace = convertView.findViewById(R.id.textView_PopulatedPlace);
            TextView textView_FirstName = convertView.findViewById(R.id.textView_FirstName);
            TextView textView_LastName = convertView.findViewById(R.id.textView_LastName);
            TextView textView_Age = convertView.findViewById(R.id.textView_Age);

            Admin admin = arrayList.get(position);
            textView_ID.setText(String.valueOf(admin.getId()));
            textView_Username.setText(admin.getUsername());
            textView_Password.setText(admin.getPassword());
            textView_Address.setText(admin.getAddress());
            textView_PopulatedPlace.setText(admin.getPopulated_place());
            textView_FirstName.setText(admin.getFirst_name());
            textView_LastName.setText(admin.getLast_name());
            textView_Age.setText(admin.getAge());


        return convertView;
    }
}


