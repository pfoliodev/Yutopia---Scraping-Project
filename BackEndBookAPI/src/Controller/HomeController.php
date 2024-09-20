<?php

namespace App\Controller;

use App\Repository\BookRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class HomeController extends AbstractController 
{
    #[Route("/", name: "home")]
    function index (BookRepository $bookRepository): Response {
        $books = $bookRepository->findAll();
        return $this->render('home/index.html.twig', [
            'books' => $books
        ]);
    }

    #[Route("/{id}", name: "book.show")]
    function show (int $id, BookRepository $bookRepository): Response {
        $book = $bookRepository->find($id);
        return $this->render('home/show.html.twig', [
            'book' => $book
        ]);
    }
}
