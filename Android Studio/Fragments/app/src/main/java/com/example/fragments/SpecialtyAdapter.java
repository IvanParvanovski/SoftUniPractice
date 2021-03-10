package com.example.fragments;

import android.content.Context;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

public class SpecialtyAdapter extends FragmentPagerAdapter {
    private Context mContext;

    public SpecialtyAdapter(Context mContext, FragmentManager fm) {
        super(fm);
        this.mContext = mContext;
    }

    @Override
    public Fragment getItem(int position) {
        if (position == 0) {
            return new Fragment1();

        } else if (position == 1) {
            return new Fragment2();

        } else {
            return new Fragment3();
        }

    }

    @Override
    public CharSequence getPageTitle(int position)
    {
      if(position == 0)
      {
          return mContext.getString(R.string.specialty_information);
      } else if (position == 1) {
          return mContext.getString(R.string.specialty_it);
      } else {
          return mContext.getString(R.string.specialty_multimedia);
      }

    }

    @Override
    public int getCount() {
        return 0;
    }
}
