{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python37Packages.discordpy
    pkgs.python37Packages.pyyaml
    pkgs.python37Packages.structlog
  ];
}
