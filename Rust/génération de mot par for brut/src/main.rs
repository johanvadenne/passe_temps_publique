fn main() {
    let mut total_combinations: usize = 0;

    for length in 1..=100 {
        let mut mot: Vec<char> = vec!['a'; length];

        loop {
            total_combinations += 1;

            if total_combinations % 1_000_000_000 == 0 {
                println!("{}", mot.iter().collect::<String>());
            }

            // Incrémente le mot
            if !increment_mot(&mut mot) {
                break; // Fin des combinaisons
            }
        }
    }
}

// Fonction pour incrémenter le mot
fn increment_mot(mot: &mut Vec<char>) -> bool {
    let len: usize = mot.len();
    let mut index: usize = len - 1; // Commence à la fin du mot

    while index < len {
        // Incrémente la lettre
        if mot[index] == 'z' { // Si c'est le dernier caractère de l'alphabet
            mot[index] = 'a'; // Réinitialise à 'a'
        } else {
            mot[index] = (mot[index] as u8 + 1) as char; // Incrémente le caractère
            return true; // Continue à incrémenter
        }
        index -= 1; // Passe au caractère précédent
    }

    false // Si tous les caractères sont réinitialisés
}
