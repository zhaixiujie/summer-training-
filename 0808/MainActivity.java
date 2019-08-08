package com.example.day2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.nfc.Tag;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity {

    private Button startNormalActivity;
    private Button startDialogActivity;//定义两个按钮
    private Button button;//初始化button
    private String TAG="MainActivity";


    @Override//重写
    protected void onCreate(Bundle savedInstanceState) {//oncreate方法
        super.onCreate(savedInstanceState);
        Log.d(TAG,"onCreate");
        setContentView(R.layout.activity_main);
        startNormalActivity=findViewById(R.id.start_normal_activity);
        startDialogActivity=findViewById(R.id.start_dialog_activity);//找到两个按钮
        final Intent localIntent = new Intent(MainActivity.this, NormalActivity.class);
        Timer timer = new Timer();
        TimerTask tast = new TimerTask() {
            @Override
            public void run() {
                startActivity(localIntent);
            }
        };
        timer.schedule(tast, 2000);
        startDialogActivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //建立一个Intent意图，startActivity完成界面跳转
                Intent intent=new Intent(MainActivity.this,Dialogctivity.class);
                startActivity(intent);
            }
        });
        startNormalActivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent=new Intent(MainActivity.this,NormalActivity.class);
                startActivity(intent);
            }
        });

//        initView();
//    }

//    private void initView() {
//        button = findViewById(R.id.button);//必须放在第三个，因为第二个是加载布局，布局都没找到怎么找button
//        button.setOnClickListener(new View.OnClickListener() { //点击事件
//            @Override
//            public void onClick(View view) {
//                AlertDialog.Builder dialog = new AlertDialog.Builder(MainActivity.this);
//                dialog.setTitle("同学们辛苦了");
//                dialog.setMessage("我可能太菜了");
//                dialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
//                    @Override
//                    public void onClick(DialogInterface dialogInterface, int i) {
//                        Toast.makeText(MainActivity.this, "哈哈我就是菜", Toast.LENGTH_LONG).show();
//                    }
//                });
//                dialog.setNegativeButton("取消", new DialogInterface.OnClickListener() {
//                    @Override
//                    public void onClick(DialogInterface dialogInterface, int i) {
//                        Toast.makeText(MainActivity.this, "不，我在努力", Toast.LENGTH_SHORT).show();
//                    }
//                });
//                dialog.show();
//            }
//        });
    }
}
