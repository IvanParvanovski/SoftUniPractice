import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class MyDataBaseHelper extends SQLiteOpenHelper {

    //константи за конструктора на класа
//дава името на файла с база данни
    private static final String DATABASE_NAME = "my_database.db";

    //отговаря на номера на базата данни
    private static final int DATABASE_VERSION = 1;

    // конструктор на класа
    public MyDataBaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    // име на таблицата
    public final static String TABLE_NAME = "users";

    // индентификатор на потребителя
    public final static String UID = "_ID";

    // име на потребителя
    public final static String COLUMN_USER_NAME = "uname";

    //създаване на базата данни
    @Override
    public void onCreate(SQLiteDatabase database) {
        String SQL_CREATE_ITEMS_TABLE = "CREATE TABLE "
                + TABLE_NAME + " ("
                + UID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                + COLUMN_USER_NAME + " TEXT NOT NULL);";

        // изпълнение на SQL оператора
        database.execSQL(SQL_CREATE_ITEMS_TABLE);

    }

    //обновяване на базата данни
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // изтриваме предходната таблица при обновяването
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_NAME);

        // създаваме нов екземпляр от таблицата
        onCreate(db);

    }

}