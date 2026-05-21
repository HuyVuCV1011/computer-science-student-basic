# Import thư viện chứa data
import data as d


def addStudent():
    """Hàm thêm một sinh viên"""
    print("*** THÊM SINH VIÊN ***")

    # Cấu trúc lưu trữ một sinh viên
    infor = {
        'id': '',
        'name': '',
        'sex': '',
        'age': '',
        'GPA': ''
    }

    # Nhập ID, có kiểm tra trùng ID thì nhập lại
    print("Nhập ID sinh viên:")
    id = input()

    while True:
        student = findStudent(id)
        if student != False:
            print("ID này đã tồn tại, vui lòng nhập lại:")
            id = input()
        else:
            break

    infor['id'] = id

    # Nhập tên
    print("Nhập tên sinh viên:")
    infor['name'] = input()

    # Nhập giới tính
    print("Nhập giới tính sinh viên:")
    sex = input()
    while True:
        if sex != "male" and sex != "female":
            print("Giới tính không tồn tại, vui lòng nhập lại:")
            sex = input()
        else:
            break
    infor['sex'] = sex

    # Nhập tuoi
    print("Nhập tuổi sinh viên:")
    infor['age'] = input()

    # Nhập tên
    print("Nhập GPA sinh viên:")
    infor['GPA'] = input()

    # Lưu vào danh sách sv
    d.listStudents.append(infor)


def findStudent(id):
    """Hàm tìm một sinh viên"""
    for i in range(0, len(d.listStudents)):
        if d.listStudents[i]['id'] == id:
            # Trả về mảng gồm 2 phần tử,
            # 0 là vị trí tìm thấy và 1 là dữ liệu
            return [i, d.listStudents[i]]
    return False


def deleteStudent():
    """Hàm xóa sih viên"""
    print("*** XÓA SINH VIÊN ***")
    print("Nhập ID sinh viên cần xóa:")
    id = input()

    student = findStudent(id)

    if student != False:
        d.listStudents.remove(student[1])
        print("Xóa sinh viên thành công")
    else:
        print("Không tìm thấy sinh viên cần xóa")


def showStudents():
    """Hàm hiển thị danh sách sv"""
    print("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***")
    print("[ ID ] [ Name ] [ Sex ] [ Age ] [ GPA ]")
    for i in range(0, len(d.listStudents)):
        print("[", d.listStudents[i]['id'], "]", "[", d.listStudents[i]['name'], "]", "[", d.listStudents[i]['sex'],
              "]", "[", d.listStudents[i]['age'], "]", "[", d.listStudents[i]['GPA'], "]")


def editStudent():
    """Hàm sửa sinh viên"""
    print("*** SỬA THÔNG TIN SINH VIÊN ***")
    print("Nhập ID sinh viên cần sửa")
    id = input()
    student = findStudent(id)
    if student == False:
        print("Không tìm thấy sinh viên ", id)
    else:

        action = 0

        # tao cac dieu kien de thay doi
        while action >= 0:
            if action == 1:
                name = input()
                student[1]['name'] = name
                d.listStudents[student[0]] = student[1]
            elif action == 2:
                sex = input()
                student[1]['sex'] = sex
                d.listStudents[student[0]] = student[1]
            elif action == 3:
                age = input()
                student[1]['age'] = age
                d.listStudents[student[0]] = student[1]
            elif action == 4:
                GPA = input()
                student[1]['GPA'] = GPA
                d.listStudents[student[0]] = student[1]

            print("Chọn thông tin cần sửa")
            print("Nhập 1: Sửa tên")
            print("Nhập 2: Sửa giới tính")
            print("Nhập 3: Sửa Tuổi")
            print("Nhập 4: Sửa GPA")
            print("Nhập 0: Thoát khỏi sửa")

            action = int(input())
            if action == 0:
                break
