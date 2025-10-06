# MEMOBOARD - Your helper to play chess without a chessboard.
# Born on monday, may 6th, 2024 by Gabriele Battaglia IZ4APU.
# June 28th, 2024: moved on Github

#QI
from GBUtils import key, dgt, menu, manuale
import time, datetime, random, json, os

# CONST
VERSION="2.5.0, October 2025 by Gabriele Battaglia (IZ4APU) & Gemini 2.5 Pro"
STARTTIME=time.time()
SCORES_FILE = "memoboard_scores.json" 
# --- VARIABILI GLOBALI ---
mnu={"quit":"to quit the app",
     "help":"to read instruction on MemoBoard",
     "menu":"to read this menu",
     "knights":"Execise with knights",
     "bishops":"Exercise with diagonals",
     "colors":"This square is white or black?",
     "test":"Take your test on all skills!"}
log=open("memoboard.txt","a+") # Usiamo 'a+' che è più standard per appendere e leggere
log.write(f"\n# {time.asctime()} Hello, Memoboard {VERSION} starts.")

board_set=set()
for y in "12345678":
    for x in "ABCDEFGH":
        board_set.add(f"{x}{y}")
board=list(board_set) # <<< MODIFICATO: Creazione della scacchiera semplificata

columns={"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta",
         "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel"}

diagonals={'A1H8':['A1','B2','C3','D4','E5','F6','G7','H8'],
           'B1H7':['B1','C2','D3','E4','F5','G6','H7'],
           'C1H6':['C1','D2','E3','F4','G5','H6'],
           'D1H5':['D1','E2','F3','G4','H5'],
           'E1H4':['E1','F2','G3','H4'],
           'F1H3':['F1','G2','H3'], 'G1H2':['G1','H2'],
           'B1A2':['B1','A2'], 'C1A3':['C1','B2','A3'],
           'D1A4':['D1','C2','B3','A4'],
           'E1A5':['E1','D2','C3','B4','A5'],
           'F1A6':['F1','E2','D3','C4','B5','A6'],
           'G1A7':['G1','F2','E3','D4','C5','B6','A7'],
           'H1A8':['H1','G2','F3','E4','D5','C6','B7','A8']}

# --- FUNZIONI GESTIONE PUNTEGGI (JSON) ---

def load_scores():
    """
    Carica i punteggi dal file JSON.
    Se il file non esiste o è vuoto, ritorna un dizionario vuoto.
    """
    if not os.path.exists(SCORES_FILE):
        return {}
    try:
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Se il file è corrotto o vuoto, ritorna un dizionario vuoto
        return {}

def save_scores(scores_data):
    """
    Salva il dizionario dei punteggi nel file JSON.
    Usa indent=4 per rendere il file leggibile.
    """
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores_data, f, indent=2)
# --- FUNZIONI HELPER ---

def is_knight_move(sq1, sq2):
    """Controlla se due case sono a un salto di cavallo di distanza. Ritorna True o False."""
    if sq1 == sq2:
        return False
    dx = abs(ord(sq1[0]) - ord(sq2[0]))
    dy = abs(ord(sq1[1]) - ord(sq2[1]))
    return {dx, dy} == {1, 2}

def get_square_color(sq):
    """Determina il colore di una casa. Ritorna 'b' per nero o 'w' per bianco."""
    col = ord(sq[0]) - ord('A')
    row = ord(sq[1]) - ord('1')
    return 'b' if (col + row) % 2 == 0 else 'w'

def Prox(sq, kind, range_limit):
    '''Genera una casa vicina a 'sq' che NON sia sulla stessa diagonale (kind='B') 
       o a un salto di cavallo (kind='N').'''
    x,y = ord(sq[0])-64, ord(sq[1])-48
    x1,x2 = max(1, x-range_limit), min(8, x+range_limit)
    y1,y2 = max(1, y-range_limit), min(8, y+range_limit)
    
    while True:
        psq = chr(random.randint(x1,x2)+64) + chr(random.randint(y1,y2)+48)
        if psq == sq:
            continue

        check = False
        if kind == "B":
            found = [k for k,v in diagonals.items() if sq in v]
            for j in found:
                if psq in diagonals[j]: check = True
        else: # kind == 'N'
            check = is_knight_move(sq, psq)
        
        if not check:
            break
            
    return psq

def report_and_update_scores(all_scores, username, exercise_name, rpt, score, duration, wins):
    """
    Shows a detailed report, compares with previous results, and updates the user's data.
    """
    # 1. Prepare new results in a structured format
    new_results = {
        "score": score,
        "wins": wins,
        "repetitions": rpt,
        "duration": duration,
        "average_time_per_guess": duration / rpt if rpt > 0 else 0,
        "score_per_win": score / wins if wins > 0 else 0,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    new_results["score_per_minute"] = (score / duration) * 60 if duration > 0 else 0

    print("\n--- Exercise Results ---")
    print(f"You got {wins} correct answers out of {rpt}.")
    print(f"Total score: {score:.0f} in {duration:.1f} seconds.")
    print(f"Performance: {new_results['score_per_minute']:.0f} points per minute.")

    # 2. Retrieve previous results, if they exist
    previous_results = all_scores.get(username, {}).get(exercise_name)

    if previous_results:
        print("\n--- Detailed Comparison vs. Previous ---")
        
        header = f"{'Metric':<20} {'Previous':>12} {'Current':>12} {'Difference':<25}"
        print(header)
        print("-" * len(header))
        
        metrics_to_compare = {
            "Points per Minute": ("score_per_minute", ".0f"),
            "Total Score": ("score", ".0f"),
            "Correct Answers": ("wins", ".0f")
        }

        # <<< CORREZIONE: Rinominata la variabile 'key' in 'metric_key' per evitare conflitti
        for label, (metric_key, fmt) in metrics_to_compare.items():
            old_val = previous_results.get(metric_key, 0)
            new_val = new_results.get(metric_key, 0)
            diff = new_val - old_val
            
            if old_val != 0:
                perc_diff = (diff / old_val) * 100
                perc_str = f"({perc_diff:+.2f}%)"
            else:
                perc_str = "(N/A)"
            
            old_val_str = f"{old_val:{fmt}}"
            new_val_str = f"{new_val:{fmt}}"
            diff_str = f"{diff:+{fmt}} {perc_str}"

            row = f"{label:<20} {old_val_str:>12} {new_val_str:>12} {diff_str:<25}"
            print(row)
        
        print("-" * len(header))
        # Now this call will work because the 'key' function is no longer shadowed
        key(prompt="\nPress any key to continue...")

    # 3. Update (or create) data for the current user and exercise
    if username not in all_scores:
        all_scores[username] = {}
    all_scores[username][exercise_name] = new_results
    
    log.write(f"\n## Exercise '{exercise_name}' for {username}:")
    log.write(f"\nCorrect answers: {wins}/{rpt} in {duration:.1f}s. Score: {score:.0f}. Performance: {new_results['score_per_minute']:.0f} p/min")
def show_leaderboard(all_scores):
    """
    Shows a detailed leaderboard for a chosen exercise, sorted by points per minute.
    """
    if not all_scores:
        print("\nThere are no scores recorded yet to show a leaderboard.")
        key(prompt="\nPress any key to return to the menu...")
        return

    print("\nWhich exercise leaderboard would you like to see?")
    exercise_types = sorted(list(mnu.keys() - {'quit', 'help', 'menu', 'chart'}))
    for i, ex_type in enumerate(exercise_types, 1):
        print(f" {i}. {ex_type.capitalize()}")
    
    print("\nPress the corresponding number...")
    selected_exercise = None
    valid_choices = [str(i) for i in range(1, len(exercise_types) + 1)]
    
    while True:
        choice_char = key()
        if choice_char in valid_choices:
            selected_exercise = exercise_types[int(choice_char) - 1]
            break

    # Raccogliamo tutti i dati necessari per la visualizzazione
    leaderboard_data = []
    for user, data in all_scores.items():
        if selected_exercise in data:
            ex_data = data[selected_exercise]
            # Usiamo .get() con valori di default per la massima compatibilità
            performance = ex_data.get("score_per_minute", 0)
            reps = ex_data.get("repetitions", 0)
            wins = ex_data.get("wins", 0)
            duration = ex_data.get("duration", 0)
            timestamp = ex_data.get("timestamp", None)
            leaderboard_data.append((user, performance, reps, wins, duration, timestamp))

    if not leaderboard_data:
        print(f"\nNo scores found for the '{selected_exercise}' exercise.")
    else:
        # Ordiniamo sempre per performance (punti al minuto)
        sorted_leaderboard = sorted(leaderboard_data, key=lambda item: item[1], reverse=True)

        # <<< MODIFICA: Nuova intestazione della tabella, più dettagliata
        print(f"\n--- 🏆 LEADERBOARD: {selected_exercise.upper()} 🏆 ---")
        header = f"{'Pos':<4} {'User':<12} {'Atts':>4} {'Win%':>5} {'Time':>6} {'Score':>8} {'Date':>17}"
        print(header)
        print("-" * len(header))

        for i, item in enumerate(sorted_leaderboard, 1):
            user, performance, reps, wins, duration, timestamp = item

            # Formattiamo i dati per la visualizzazione
            user_display = user[:12]  # Tronca il nome utente a 12 caratteri
            accuracy_str = f"{(wins / reps) * 100:3.0f}%" if reps > 0 else "N/A"
            time_str = f"{int(duration // 60):02d}:{int(duration % 60):02d}"
            
            date_str = "N/A"
            if timestamp:
                try:
                    # Converte la stringa ISO in oggetto datetime e poi la formatta
                    date_obj = datetime.datetime.fromisoformat(timestamp)
                    date_str = date_obj.strftime('%Y-%m-%d %H:%M')
                except (ValueError, TypeError):
                    date_str = "Invalid Date" # Se il formato non è corretto

            # <<< MODIFICA: Stampa la riga con tutte le nuove informazioni
            row = f"{i:<4} {user_display:<12.12} {reps:>4} {accuracy_str:>5} {time_str:>6} {performance:>8.0f} {date_str:>17}"
            print(row)
        
        print("-" * len(header))

    key(prompt="\nPress any key to return to the menu...")
# --- FUNZIONI DEGLI ESERCIZI ---

def ExKnights(ripetitions):
    '''Exercise on knights'''
    score=0; wins=0; scoretime=15
    timeex=time.time()
    timeslist=[]; scoreslist=[]
    
    knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    while ripetitions > 0:
        sq1 = random.choice(board)
        yes = random.choice([True,False])
        
        if not yes: 
            sq2 = Prox(sq1, 'N', range_limit=2)
        else:
            x, y = ord(sq1[0]), ord(sq1[1])
            possible_sq2 = []
            for dx, dy in knight_moves:
                new_x, new_y = x + dx, y + dy
                if ord('A') <= new_x <= ord('H') and ord('1') <= new_y <= ord('8'):
                    possible_sq2.append(f"{chr(new_x)}{chr(new_y)}")
            if not possible_sq2: continue # Se il cavallo è bloccato, salta il turno
            sq2 = random.choice(possible_sq2)

        print(f"\n{columns[sq1[0]]} {sq1[1]} and {columns[sq2[0]]} {sq2[1]}",end="",flush=True)
        time.sleep(.8)
        now=time.time()
        s=key().lower()
        singlescore = (scoretime*1000) - (time.time()-now)*1000
        if singlescore < 0: singlescore = 0
        
        correct = (s=="y" and yes) or (s=="n" and not yes)
        if correct:
            wins+=1
            score+=singlescore
            scoreslist.append(singlescore)
            timeslist.append(time.time()-now)

        ripetitions-=1
        
    duration=time.time()-timeex
    return score,scoreslist,duration,timeslist,wins

def ExBishops(ripetitions):
    '''Exercise on bishops'''
    score=0; wins=0; scoretime=15
    timeex=time.time()
    timeslist=[]; scoreslist=[]
    while ripetitions>0:
        kd=random.choice(list(diagonals.keys()))
        sq1=random.choice(diagonals[kd])
        yes=random.choice([True,False])
        if not yes: sq2=Prox(sq1,'B', range_limit=3)
        else:
            while True:
                sq2=random.choice(diagonals[kd])
                if sq1!=sq2: break
        print(f"\n{columns[sq1[0]]} {sq1[1]} and {columns[sq2[0]]} {sq2[1]}",end="",flush=True)
        time.sleep(.8)
        now=time.time()
        s=key().lower()
        singlescore = (scoretime*1000)-(time.time()-now)*1000
        if singlescore<0: singlescore=0
        
        correct = (s=="y" and yes) or (s=="n" and not yes)
        if correct:
            wins+=1
            score+=singlescore
            scoreslist.append(singlescore)
            timeslist.append(time.time()-now)
        ripetitions-=1
    duration=time.time()-timeex
    return score,scoreslist,duration,timeslist,wins

def ExColors(ripetitions):
    '''Exercise on colors'''
    score=0; wins=0; scoretime=15
    timeex=time.time()
    timeslist=[]; scoreslist=[]
    while ripetitions>0:
        sq = random.choice(board)
        print(f"\n{columns[sq[0]]} {sq[1]} ",end="",flush=True)
        time.sleep(.8)
        now = time.time()
        s = key().lower()
        singlescore = (scoretime*1000)-(time.time()-now)*1000
        if singlescore < 0: singlescore = 0
        
        if s == get_square_color(sq):
            wins+=1
            score+=singlescore
            scoreslist.append(singlescore)
            timeslist.append(time.time()-now)
        
        ripetitions-=1
        
    duration = time.time()-timeex
    return score,scoreslist,duration,timeslist,wins

def main():
    # <<< MODIFICA: Carica i punteggi e chiede il nome utente all'inizio
    all_scores = load_scores()
    print(f"Welcome to MemoBoard.\nYour helper to play chess without chessboard.\nThis utility helps you to manage your chessboard and to become a better chess player.\n\tVersion {VERSION}.")
    username = input("\nPlease give me your name: ").strip().title()
    if not username:
        username = "DefaultUser"
    print(f"\nWelcome back, {username}! Ready to train? Type 'help' or 'menu'.")
    
    mnu["chart"] = "Show the leaderboard"
    while True:
        s=menu(d=mnu, ntf="Command not found", show=True, keyslist=True)
        if s=="quit": break
        
        elif s=="colors":
            print("Guess the square color.\n Please answer by pressing B for black and W for white.")
            rpt=dgt(prompt="\nNice and good luck with colors, how many guesses you want to take? ",kind="i",imin=5,imax=150)
            key(prompt="Go?")
            print(" Start")
            score,scoreslist,duration,timeslist,wins = ExColors(rpt)
            # <<< MODIFICA: Usa la nuova funzione di report
            report_and_update_scores(all_scores, username, "colors", rpt, score, duration, wins)

        elif s=="knights":
            print("Guess if these two squares are on a knight's jump.\n Please answer by pressing Y for yes and N for no.")
            rpt=dgt(prompt="\nGood and have fun with knight's jump, how many guesses you want to take? ",kind="i",imin=5,imax=150)
            key(prompt="Go?")
            print(" Start")
            score,scoreslist,duration,timeslist,wins = ExKnights(rpt)
            # <<< MODIFICA: Usa la nuova funzione di report
            report_and_update_scores(all_scores, username, "knights", rpt, score, duration, wins)
            
        elif s=="bishops":
            print("Guess if these two squares are on the same diagonal.\n Please answer by pressing Y for yes and N for no.")
            rpt=dgt(prompt="\nGood and have fun with Bishop's exercise, how many guesses you want to take? ",kind="i",imin=5,imax=150)
            key(prompt="Go?")
            print(" Start")
            score,scoreslist,duration,timeslist,wins = ExBishops(rpt)
            # <<< MODIFICA: Usa la nuova funzione di report
            report_and_update_scores(all_scores, username, "bishops", rpt, score, duration, wins)

        # <<< AGGIUNGI: Nuovo blocco per la chart
        elif s=="chart":
            show_leaderboard(all_scores)

        elif s=="help": manuale(nf="README.md")
        elif s=="menu": menu(d=mnu,show=True)
        
        elif s=="test":
            # Qui puoi integrare la stessa logica anche per il test
            print("Funzione test non ancora integrata con il nuovo sistema di punteggio.")
            pass 
    
    # <<< MODIFICA: Salva tutti i punteggi prima di uscire
    save_scores(all_scores)
    
    endtime=time.time()-STARTTIME
    print(f"\nMemoboard {VERSION}, ran for {int(endtime/60)} minutes and {int(endtime%60)} seconds.\n\tPlease check memoboard.txt Bye-Bye")
    log.write(f"\n### Goodbye from Memoboard {VERSION}, ran for {int(endtime/60)} minutes and {int(endtime%60)} seconds.\n")
    log.close()
if __name__ == "__main__":
    main()