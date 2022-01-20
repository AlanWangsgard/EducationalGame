import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;

import javax.swing.*;

public class EndFrame implements MouseListener{
	private JFrame frame;
    private drawingPanel panel;
    private final int W = 800;
    private final int HT = 800;
    private Scanner scan;
	private PrintWriter writer;
	private int[] scores;
	private int nDigits;
    
    public EndFrame() {
    	frame = new JFrame("End");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new drawingPanel();
        panel.setPreferredSize(new Dimension(W, HT));
        frame.getContentPane().add(panel);
        frame.pack();
        panel.setBackground(Color.getHSBColor(.65f, .5f, 1f));
        panel.addMouseListener(this);
    }
    
    public void visible(boolean b){
    	if(b){
			// This frame is becoming visible, get it ready!
			// Open the file.
    		try {
				scan = new Scanner(new File("scores.txt"));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
    		scores = new int[5];
    		nDigits = 0;
			// Read in the scores, and estimate the length of the string of scores.
    		for (int x = 0; x < 5; x++){
    			scores[x] = scan.nextInt();
    			nDigits += (int)(Math.log10(scores[x])) + 2;
    		}
    		scan.close();
			// Get ready to print the top 5 scores.
    		try {
				writer = new PrintWriter("scores.txt", "utf-8");
			} catch (FileNotFoundException | UnsupportedEncodingException e) {
				e.printStackTrace();
			}
			// The following is some overly-complicated but extra-efficient code to insert your score
			// If your score was good enough.
    		int newS = Main.gf.getCorrect();
    		if(newS > scores[4]){
    			if(newS > scores[3]){
    				if(newS > scores[2]){
    					if(newS > scores[1]){
    						if(newS > scores[0]){
    							scores[4] = scores[3];
    							scores[3] = scores[2];
    							scores[2] = scores[1];
    							scores[1] = scores[0];
    							scores[0] = newS;
    						}else{
    							scores[4] = scores[3];
    							scores[3] = scores[2];
    							scores[2] = scores[1];
    							scores[1] = newS;
    						}
    					}else{
    						scores[4] = scores[3];
    						scores[3] = scores[2];
    						scores[2] = newS;
    					}
    				}else{
    					scores[4] = scores[3];
    					scores[3] = newS;
    				}
    			}else{
    				scores[4] = newS;
    			}
    		}
    		writer.write(scores[0] + " " + scores[1] + " " + scores[2] + " " + scores[3] + " " + scores[4]);
    		writer.close();
    	}
    	frame.setVisible(b);
    }
    
    private class drawingPanel extends JPanel{
        public void paintComponent(Graphics g){
            super.paintComponent(g);
            g.setFont(new Font("Arial", 0, 50));
            g.setColor(Color.getHSBColor(.4f, .4f, 1f));
            g.drawString("Your Score", 230, 300);
            g.drawString("High Scores", 230, 130);
            g.setColor(Color.getHSBColor(.55f, .6f, .9f));
            g.fillRect(210, 340, 310, 50);
            g.fillRect(160, 170, 400, 50);
            g.setColor(Color.getHSBColor(.05f, .8f, 1f));
            g.drawString(Integer.toString(Main.gf.getCorrect()), 350 - 10 * (int)(Math.log10(Main.gf.getCorrect())), 382);
            String s = "";
            for (int x = 0; x < 5; x++){
            	s += scores[x] + "  ";
            }
            g.drawString(s, (int) (320 - 10*nDigits), 215);
            g.setColor(Color.getHSBColor(.4f, .8f, 1f));
            g.fillRect(170, 450, 400, 200);
            g.setColor(Color.getHSBColor(.65f, 1f, .5f));
            g.setFont(new Font("Arial", 0, 100));
            g.drawString("AGAIN!", 205, 580);
        }
    }

	@Override
	public void mouseClicked(MouseEvent arg0) {
		// Play again button.
		if (arg0.getX() > 170 && arg0.getX() < 570 && arg0.getY() > 400 && arg0.getY() < 600){
			visible(false);
			Main.gf.visible(true);
		}
	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}
}
