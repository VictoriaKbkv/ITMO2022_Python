import java.io.*;
import java.util.Random;

public class MatrixGenerator {

    public static void generateInt(int min, int max, int m, int n, File file) {
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(file, false)))) {
            Random random = new Random();
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    int number = min + random.nextInt(max-min);
                    out.print(number);
                    out.print(' ');
                }
                if (i < m-1) {out.print('\n');}
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void generateDouble(int min, int max, int m, int n, File file) {
        try (PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(file, false)))) {
            Random random = new Random();
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    double number = min + max*random.nextDouble();
                    out.print(number);
                    out.print(' ');
                }
                if (i < m-1) {out.print('\n');}
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static double[] getCoef(File file, int numberOfCoef) {
        double [] coef = new double[numberOfCoef];
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            String line;
            int lineCount = 0;
            while ((line = reader.readLine()) != null){
                coef[lineCount] = Double.parseDouble(line);
                lineCount++;
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return coef;
    }
}
