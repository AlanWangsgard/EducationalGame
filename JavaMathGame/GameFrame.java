import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.*;

public class GameFrame implements KeyListener{
	private JFrame frame;
    private drawingPanel panel;
    private final int W = 1200;
    private final int HT = 700;
    private int num1;
    private int num2;
    private int ans;
    private Timer time;
    private Timer tStart;
    private int tCount;
    private int correct;
    private int tLimit;
    public boolean add = true;
    public boolean minus;
    public boolean mult;
    public boolean div;
    
    public GameFrame() {
    	tLimit = 20;
    	frame = new JFrame("Math Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new drawingPanel();
        panel.setPreferredSize(new Dimension(W, HT));
        frame.getContentPane().add(panel);
        frame.pack();
        panel.setBackground(Color.getHSBColor(.1f, .6f, 1f));
        frame.addKeyListener(this);
        panel.setFont(new Font("Arial", 0, 200));
        correct = 0;
		// This timer puts a 200ms delay between the user's correct answer and a new question.
		// That way they have some visual feedback that it's correct.
        time = new Timer(200, null);
        time.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
        		newNums();
        		time.stop();
        	}
        });
		// This timer runs the 3..2..1.. countdown and when the game ends.
		tStart = new Timer(1000, null);
        tStart.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
        		tCount++;
        		if (tCount == 3){
					// The beginning countdown is finished.
        			newNums();
        			tStart.start();
        		}else if (tCount == 3 + tLimit){
					// The game is over.
        			visible(false);
        			Main.ef.visible(true);
        		}else{
					// Nothing special, just increments the time by one.
        			tStart.start();
        		}
        		panel.repaint();
        	}
        });
    }
    
    public void newNums(){
		// Generate some new numbers for the user.
    	panel.setBackground(Color.getHSBColor(.1f, .6f, 1f));
		ans = 0;
		if (add){
    	    num1 = (int) (Math.random() * 10);
    	    num2 = (int) (Math.random() * 10);
		}
    	panel.repaint();
    }
    
    public int getCorrect(){
		// Number of correct answers.
    	return correct;
    }
    
    public void visible(boolean b){
    	frame.setVisible(b);
    	if (b){
    		correct = 0;
			tCount = 0;
    		tStart.start();
    	}
    }
    
    private class drawingPanel extends JPanel{
        public void paintComponent(Graphics g){
        	g.setFont(new Font("Arial", 0, 200));
            super.paintComponent(g);
            if (tCount < 3){
				// Draw the countdown timer.
            	g.drawString(Integer.toString(3 - tCount), 500, 300);
            }else{
				// Draw the math problem and a timer.
            	g.drawString(Integer.toString(num1), 500, 200);
            	g.drawString("+  " + Integer.toString(num2), 270, 400);
            	g.drawString("_____", 200, 420);
            	if (ans != 0){
            		g.drawString(Integer.toString(ans), 510 - (int)(Math.log10(ans)) * 111, 640);
            	}
            	g.setFont(new Font("Arial", 0, 50));
            	g.drawString("Score: " + Integer.toString(correct), 20, 100);
            	g.drawString("Time Left", 900, 50);
            	g.drawString(Integer.toString(tLimit + 3 - tCount), 990, 100);
				// This is how I draw the timer bar.
            	g.setColor(Color.green);
            	g.fillRect(970, 120, 100, 500);
            	g.setColor(Color.red);
            	g.fillRect(970, 620 - 500 * (tCount - 3) /(tLimit), 100, 500 * (tCount - 3) / (tLimit));
            }
        }
    }
    
	@Override
	public void keyPressed(KeyEvent arg0) {
		// The user pressed a key. What should we do about it?
		if (arg0.getKeyCode()>47 && arg0.getKeyCode() < 58){
			// Add a new number from number row.
			ans *= 10;
			ans += arg0.getKeyChar() - 48;
		}else if (arg0.getKeyCode() > 95 && arg0.getKeyCode() < 106){
			// Add a new number from the numpad.
			ans *= 10;
			ans += arg0.getKeyCode() - 96;
		}else if (arg0.getKeyCode() == 127 || arg0.getKeyCode() == 8){
			// Delete last entered number.
			ans = ans / 10;
		}
		if (ans == num1 + num2){
			// Their answer is correct, show a reward.
			panel.setBackground(Color.getHSBColor(.35f, .7f, 1f));
			correct++;
			panel.repaint();
			time.start();
		}
		panel.repaint();
	}

	@Override
	public void keyReleased(KeyEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyTyped(KeyEvent arg0) {
		// TODO Auto-generated method stub
		
	}
}
