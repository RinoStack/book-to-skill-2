#!/usr/bin/env python3
import click

@click.command()
@click.argument('pdf_file')
def convert_book(pdf_file):
    """Convert PDF to Claude Code skill"""
    click.echo(f"Converting {pdf_file} to skill...")

if __name__ == '__main__':
    convert_book()