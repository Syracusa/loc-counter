repository_domain="https://github.com/Syracusa/"
projects=()
projects+=("bbb-dd-examples")
projects+=("sy-technotes")
projects+=("sy-misc")
projects+=("sy_cpp_boilerplate")
projects+=("pywebsock-boilerplate")
projects+=("sy-angular-boilerplate")
projects+=("linux-c-boilerplate")
projects+=("VolatileTextEditor")
projects+=("source-graph")
projects+=("sy-msg-window")
projects+=("sy-rust-boilerplate")
projects+=("my-openssl-examples")
projects+=("time-wheel")
projects+=("CodingTest")

for prj in ${projects[@]}; do
    git submodule add ${repository_domain}${prj} ./projects/${prj}
done

mkdir -p log
python3 src/main.py 

cp ./log/*.json ./webgui/src/assets/

# git submodule add https://github.com/Syracusa/bbb-dd-examples ./projects/bbb-dd-examples
