let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python37Packages.discordpy
    pkgs.python37Packages.pyyaml
    pkgs.python37Packages.structlog
  ];
}
