use actix_files as fs; // Pour servir des fichiers statiques
use actix_web::{web, App, HttpResponse, HttpServer, Responder};

async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Bonjour depuis Rust!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(fs::Files::new("/", "./static").index_file("index.html")) // Servir le dossier statique
            .route("/hello", web::get().to(hello)) // Exemple de route
    })
    .bind("127.0.0.1:8080")? // Adresse et port à lier
    .run()
    .await
}
