package com.example.actividad1;

import android.animation.ObjectAnimator;
import android.os.Bundle;
import android.os.VibrationEffect;
import android.os.Vibrator;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private ListView listView;
    private CustomAdapter adapter;
    private List<Item> itemList;
    Button button;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listView = findViewById(R.id.listView);
        View button = findViewById(R.id.button);

        // Crear lista de ejemplos
        itemList = new ArrayList<>();
        for (int i = 1; i <= 20; i++) {
            itemList.add(new Item("Elemento " + i, "Descripción del elemento " + i));
        }

        // Crear y establecer el adapter
        adapter = new CustomAdapter(this, itemList);
        listView.setAdapter(adapter);

        // Listener para los clicks en los items
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Item selectedItem = itemList.get(position);
                Toast.makeText(MainActivity.this,
                        "Seleccionado: " + selectedItem.getTitle(),
                        Toast.LENGTH_SHORT).show();
            }
        });

        // 👇 Aquí colocas el botón con el efecto espectacular
        button.setOnClickListener(v -> {
            // Vibración
            Vibrator vibrator = (Vibrator) getSystemService(VIBRATOR_SERVICE);
            if (vibrator != null && vibrator.hasVibrator()) {
                vibrator.vibrate(VibrationEffect.createOneShot(150, VibrationEffect.DEFAULT_AMPLITUDE));
            }

            // Animación fade in
            ObjectAnimator animator = ObjectAnimator.ofFloat(listView, "alpha", 0f, 1f);
            animator.setDuration(500);
            animator.start();

            // Mostrar mensaje
            new AlertDialog.Builder(this)
                    .setTitle("¡Efecto espectacular! 🚀")
                    .setMessage("Has hecho clic en el botón de manera épica 😎")
                    .setPositiveButton("OK", null)
                    .show();
        });


    }
    
}