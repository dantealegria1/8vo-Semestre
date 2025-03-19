package com.example.actividad2.customviews;

import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Rect;
import android.util.AttributeSet;
import android.view.View;

import com.example.actividad2.R;

public class MiVistaPersonalizada extends View {
    private String titulo;
    private int colorFondo;
    private float tamanoTexto;
    private Paint paintFondo;
    private Paint paintTexto;

    public MiVistaPersonalizada(Context context) {
        super(context);
        init(null);
    }

    public MiVistaPersonalizada(Context context, AttributeSet attrs) {
        super(context, attrs);
        init(attrs);
    }

    public MiVistaPersonalizada(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init(attrs);
    }

    private void init(AttributeSet attrs) {
        // Valores predeterminados
        titulo = "Vista Personalizada";
        colorFondo = Color.LTGRAY;
        tamanoTexto = 40f;

        // Obtener atributos personalizados del XML
        if (attrs != null) {
            TypedArray a = getContext().obtainStyledAttributes(attrs, R.styleable.MiVistaPersonalizada);

            // Leer atributos
            titulo = a.getString(R.styleable.MiVistaPersonalizada_titulo);
            colorFondo = a.getColor(R.styleable.MiVistaPersonalizada_colorFondo, colorFondo);
            tamanoTexto = a.getDimension(R.styleable.MiVistaPersonalizada_tamanoTexto, tamanoTexto);

            // Liberar recursos
            a.recycle();
        }

        // Inicializar pinturas
        paintFondo = new Paint();
        paintFondo.setColor(colorFondo);
        paintFondo.setStyle(Paint.Style.FILL);

        paintTexto = new Paint();
        paintTexto.setColor(Color.BLACK);
        paintTexto.setTextSize(tamanoTexto);
        paintTexto.setTextAlign(Paint.Align.CENTER);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);

        // Dibujar fondo
        canvas.drawRect(0, 0, getWidth(), getHeight(), paintFondo);

        // Dibujar texto
        int xPos = getWidth() / 2;
        int yPos = (int) ((getHeight() / 2) - ((paintTexto.descent() + paintTexto.ascent()) / 2));
        canvas.drawText(titulo, xPos, yPos, paintTexto);
    }

    // Métodos para cambiar propiedades en tiempo de ejecución
    public void setTitulo(String titulo) {
        this.titulo = titulo;
        invalidate();
    }

    public void setColorFondo(int color) {
        this.colorFondo = color;
        paintFondo.setColor(color);
        invalidate();
    }

    public void setTamanoTexto(float tamano) {
        this.tamanoTexto = tamano;
        paintTexto.setTextSize(tamano);
        invalidate();
    }
}